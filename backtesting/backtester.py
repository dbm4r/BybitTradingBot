from backtesting.portfolio import Portfolio
from backtesting.execution_manager import ExecutionManager
from backtesting.performance.statistics import Statistics
from core.settings import Settings
from backtesting.performance.equity_curve import EquityCurve
from backtesting.performance.risk_metrics import RiskMetrics



class Backtester:

    def __init__(self, settings, symbol, strategy):

        self.settings = settings

        self.portfolio = Portfolio(
            settings.initial_balance
        )

        self.execution = ExecutionManager(
            portfolio=self.portfolio,
            settings=settings
        )

        self.engine = self.execution.get_engine(
            symbol,
            strategy
        )

        self.symbol = symbol
        self.strategy = strategy
        self.equity = EquityCurve()

        self.trades = []

    def run(self, df):

        engine = self.engine

        for _, row in df.iterrows():

            signal = row["signal"]
            price = row["close"]
            timestamp = row["timestamp"]
            engine.order_manager.process_pending_orders(
                engine,
                row)

            engine.process_candle(row)

            portfolio_value = self.portfolio.total_value(
                self.symbol,
                row["close"])

            self.equity.add(
                row["timestamp"],
                portfolio_value)
            

        # Close any remaining open position
        if self.portfolio.in_position(self.symbol):

            last_row = df.iloc[-1]

            engine.sell(
                timestamp=last_row["timestamp"],
                price=last_row["close"],
                exit_reason="End of Backtest"
            )

            self.equity.add(
                last_row["timestamp"],
                self.portfolio.total_value(
                    self.symbol,
                    last_row["close"]
                )
            )

        self.trades = engine.trades

        curve = self.equity.dataframe()
        curve.to_csv("results/equity_curve.csv", index=False)

        return self.trades

    def print_report(self):

        print("\n========== STRATEGY COMPARISON ==========\n")

        ranked = sorted(
            self.results,
            key=lambda result: result.roi,
            reverse=True
        )

        for result in ranked:

            print(
                f"{result.strategy:<20}"
                f"ROI {result.roi:>8.2f}%   "
                f"Profit ${result.net_profit:>10.2f}   "
                f"Win {result.win_rate:>6.2f}%   "
                f"Trades {result.trades:>4}   "
                f"DD {result.max_drawdown:>7.2f}%"
            )