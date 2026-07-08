from backtesting.backtester import Backtester
from backtesting.comparison.comparison_result import ComparisonResult
from backtesting.performance.statistics import Statistics
from backtesting.performance.risk_metrics import RiskMetrics
from backtesting.performance.equity_curve import EquityCurve


class ComparisonRunner:

    def __init__(
        self,
        settings,
        symbol
    ):

        self.settings = settings
        self.symbol = symbol

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

            strategy_dataframe = dataframe.copy()

            strategy_dataframe = (
                strategy.generate_signals(
                    strategy_dataframe
                )
            )

            backtester = Backtester(
                settings=self.settings,
                symbol=self.symbol,
                strategy=strategy
            )

            trades = backtester.run(
                strategy_dataframe
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