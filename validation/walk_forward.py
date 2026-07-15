from optimization.optimizer import Optimizer
from validation.window_splitter import WindowSplitter
from strategies.framework.strategy_factory import StrategyFactory
from backtesting.backtester import Backtester
from validation.walk_forward_result import WalkForwardResult
from backtesting.performance.statistics import Statistics


class WalkForwardValidator:

    def __init__(
        self,
        settings,
        symbol,
    ):

        self.settings = settings
        self.symbol = symbol

        self.optimizer = Optimizer(
            settings=settings,
            symbol=symbol,
        )

        self.splitter = WindowSplitter()

        self.results = []

    def validate(
        self,
        dataframe,
        strategy_name,
        parameter_grid,
        train_size,
        test_size,
    ):

        self.clear()

        windows = self.splitter.split(
            dataframe=dataframe,
            train_size=train_size,
            test_size=test_size,
        )

        for index, window in enumerate(windows):

            self.optimizer.optimize(
                dataframe=window.train,
                strategy_name=strategy_name,
                parameter_grid=parameter_grid,
            )

            best = self.optimizer.best_result()

            strategy = StrategyFactory.create(
                strategy_name,
                **best.parameters,
            )

            backtester = Backtester(
                settings=self.settings,
                symbol=self.symbol,
                strategy=strategy,
            )

            trades = backtester.run(
                window.test,
            )

            result = WalkForwardResult(
                strategy=strategy.name,

                parameters=best.parameters,

                train_roi=best.roi,

                test_roi=self.calculate_roi(
                    backtester
                ),

                train_profit=best.net_profit,

                test_profit=Statistics.total_profit(
                    trades
                ),

                train_trades=best.trades,

                test_trades=Statistics.total_trades(
                    trades
                ),
            )

            self.results.append(result)

        return self.results

    @staticmethod
    def calculate_roi(
        backtester,
    ):

        return (
            (
                backtester.portfolio.cash
                - backtester.portfolio.initial_balance
            )
            /
            backtester.portfolio.initial_balance
        ) * 100

    def clear(self):

        self.results.clear()

    def all_results(self):

        return self.results

    def best_result(self):

        if not self.results:

            return None

        return max(
            self.results,
            key=lambda result: result.test_roi,
        )
    def summary(self):

        if not self.results:

            return None

        train_roi = [
            result.train_roi
            for result in self.results
        ]

        test_roi = [
            result.test_roi
            for result in self.results
        ]

        return {

            "windows": len(self.results),

            "average_train_roi": (
                sum(train_roi)
                / len(train_roi)
            ),

            "average_test_roi": (
                sum(test_roi)
                / len(test_roi)
            ),

            "best_test_roi": max(test_roi),

            "worst_test_roi": min(test_roi),

            "positive": len(
                [
                    roi
                    for roi in test_roi
                    if roi > 0
                ]
            ),

            "negative": len(
                [
                    roi
                    for roi in test_roi
                    if roi <= 0
                ]
            )

        }
    def passed(self):

        summary = self.summary()

        if summary is None:
            return False

        return (

            summary["average_test_roi"] > 0

            and

            summary["positive"] >= (
                summary["windows"] * 0.60
            )

        )

    def print_report(self):

        print(
            "\n========== WALK FORWARD ==========\n"
        )

        for index, result in enumerate(
            self.results,
            start=1,
        ):

            print(f"Window {index}")

            print(
                f"Parameters : {result.parameters}"
            )

            print(
                f"Train ROI  : {result.train_roi:.2f}%"
            )

            print(
                f"Test ROI   : {result.test_roi:.2f}%"
            )

            print(
                f"Train Profit : ${result.train_profit:.2f}"
            )

            print(
                f"Test Profit  : ${result.test_profit:.2f}"
            )

            print(
                f"Train Trades : {result.train_trades}"
            )

            print(
                f"Test Trades  : {result.test_trades}"
            )

            print()
            summary = self.summary()

            print(
                "========== SUMMARY ==========\n"
            )

            print(
                f"Windows            : {summary['windows']}"
            )

            print(
                f"Average Train ROI  : "
                f"{summary['average_train_roi']:.2f}%"
            )

            print(
                f"Average Test ROI   : "
                f"{summary['average_test_roi']:.2f}%"
            )

            print(
                f"Best Test ROI      : "
                f"{summary['best_test_roi']:.2f}%"
            )

            print(
                f"Worst Test ROI     : "
                f"{summary['worst_test_roi']:.2f}%"
            )

            print(
                f"Positive Windows   : "
                f"{summary['positive']}"
            )

            print(
                f"Negative Windows   : "
                f"{summary['negative']}"
            )
            print()

            print(
                "Validation Status :",
                "PASSED"
                if self.passed()
                else "FAILED"
            )
