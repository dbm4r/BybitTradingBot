from backtesting.runner.backtest_runner import BacktestRunner
from backtesting.comparison.comparison_result import ComparisonResult
from backtesting.performance.statistics import Statistics
from backtesting.performance.risk_metrics import RiskMetrics


class ComparisonRunner:

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

    def compare(
        self,
        dataframe,
        strategies
    ):

        self.results.clear()

        for strategy in strategies:

            print(
                f"\nRunning {strategy.name}..."
            )

            backtester, trades = self.runner.run(
                dataframe,
                strategy
            )

            curve = backtester.equity.dataframe()

            result = ComparisonResult(
                strategy=strategy.name,
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
                ),
                roi=(
                    (
                        backtester.portfolio.cash
                        - backtester.portfolio.initial_balance
                    )
                    /
                    backtester.portfolio.initial_balance
                ) * 100
            )

            self.results.append(result)

        return self.results