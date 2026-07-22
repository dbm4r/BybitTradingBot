from strategies.framework.strategy_factory import StrategyFactory
from optimization.optimization_result import OptimizationResult
from backtesting.runner.backtest_runner import BacktestRunner

from backtesting.performance.statistics import Statistics
from backtesting.performance.risk_metrics import RiskMetrics



class Optimizer:

    def __init__(
        self,
        settings,
        symbol
    ):

        self.runner = BacktestRunner(
            settings=settings,
            symbol=symbol
        )

        self.results = []

    def clear(self):

        self.results.clear()

    def add_result(
        self,
        result: OptimizationResult
    ):

        self.results.append(result)

    def all_results(self):

        return self.results

    def best_by_roi(self):

        return sorted(
            self.results,
            key=lambda result: result.roi,
            reverse=True
        )
    def best_result(
        self,
    ):

        if not self.results:

            return None

        return max(
            self.results,
            key=lambda result: result.roi,
        )

    def optimize(
        self,
        dataframe,
        strategy_name,
        parameter_grid
    ):

        self.clear()

        for parameters in parameter_grid.generate():

            strategy = StrategyFactory.create(
                strategy_name,
                **parameters
            )

            backtester, trades = self.runner.run(
                dataframe,
                strategy
            )

            curve = backtester.equity.dataframe()

            final_balance = backtester.portfolio.cash

            roi = (
                (
                    final_balance
                    - backtester.portfolio.initial_balance
                )
                /
                backtester.portfolio.initial_balance
            ) * 100

            result = OptimizationResult(

                strategy=strategy.name,

                parameters=strategy.parameters,

                roi=roi,

                net_profit=Statistics.total_profit(
                    trades
                ),

                win_rate=Statistics.win_rate(
                    trades
                ),

                trades=Statistics.total_trades(
                    trades
                ),

                max_drawdown=RiskMetrics.max_drawdown(
                    curve
                )
            )

            self.add_result(result)

        return self.results

    def print_report(self):

        print("\n========== OPTIMIZATION ==========\n")

        if not self.results:

            print("No optimization results available.")
            return

        for result in self.best_by_roi():

            print(
                f"{result.strategy:<18}"
                f"ROI {result.roi:>8.2f}%   "
                f"Profit ${result.net_profit:>10.2f}   "
                f"Win {result.win_rate:>6.2f}%   "
                f"Trades {result.trades:>4}   "
                f"DD {result.max_drawdown:>7.2f}%   "
                f"{result.parameters}"
            )