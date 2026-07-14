from backtesting.portfolio import Portfolio
from backtesting.execution_manager import ExecutionManager
from backtesting.performance.statistics import Statistics
from core.settings import Settings
from backtesting.performance.equity_curve import EquityCurve
from backtesting.performance.risk_metrics import RiskMetrics
from market.candle_factory import CandleFactory
from pipeline.trading_pipeline import TradingPipeline
from trading.trading_session import TradingSession


class Backtester:

    def __init__(self, settings, symbol, strategy, interval="1"):

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
        self.interval = interval
        self.equity = EquityCurve()

        self.trades = []

    def run(
        self,
        dataframe,
    ):

        engine = self.engine

        session = TradingSession(
            engine=engine,
            pipeline=TradingPipeline(
                strategy=self.strategy,
                symbol=self.symbol,
                interval=self.interval,
            ),
        )

        for _, row in dataframe.iterrows():

            candle = CandleFactory.from_series(
                row=row,
                symbol=self.symbol,
                interval=self.interval,
            )

            engine.order_manager.process_pending_orders(
                engine=engine,
                candle=candle,
            )

            session.process_candle(
                candle,
            )

            portfolio_value = self.portfolio.total_value(
                self.symbol,
                candle.close,
            )

            self.equity.add(
                candle.timestamp,
                portfolio_value,
            )

        if self.portfolio.in_position(
            self.symbol
        ):

            last_row = dataframe.iloc[-1]

            last_candle = CandleFactory.from_series(
                row=last_row,
                symbol=self.symbol,
                interval=self.interval,
            )

            engine.sell(
                timestamp=last_candle.timestamp,
                price=last_candle.close,
                exit_reason="End of Backtest",
            )

            self.equity.add(
                last_candle.timestamp,
                self.portfolio.total_value(
                    self.symbol,
                    last_candle.close,
                ),
            )

        self.trades = engine.trades

        curve = self.equity.dataframe()

        curve.to_csv(
            "results/equity_curve.csv",
            index=False,
        )

        return self.trades

    def print_report(self):

        curve = self.equity.dataframe()

        max_drawdown = RiskMetrics.max_drawdown(
            curve
        )

        total_profit = Statistics.total_profit(
            self.trades
        )

        total_trades = Statistics.total_trades(
            self.trades
        )

        winners = Statistics.winning_trades(
            self.trades
        )

        losers = Statistics.losing_trades(
            self.trades
        )

        win_rate = Statistics.win_rate(
            self.trades
        )

        average_win = Statistics.average_win(
            self.trades
        )

        average_loss = Statistics.average_loss(
            self.trades
        )

        engine = self.execution.get_engine(
            self.symbol,
            self.strategy
        )

        fees = engine.total_fees

        final_balance = self.portfolio.cash

        roi = (
            (
                final_balance
                - self.portfolio.initial_balance
            )
            /
            self.portfolio.initial_balance
        ) * 100

        print("\n========== BACKTEST REPORT ==========\n")

        print(
            f"Strategy        : {self.strategy.name}"
        )

        print(
            f"Initial Balance : ${self.portfolio.initial_balance:,.2f}"
        )

        print(
            f"Final Balance   : ${final_balance:,.2f}"
        )

        print()

        print(
            f"Net Profit      : ${total_profit:,.2f}"
        )

        print(
            f"Trading Fees    : ${fees:,.2f}"
        )

        print(
            f"Return          : {roi:.2f}%"
        )

        print()

        print(
            f"Trades          : {total_trades}"
        )

        print(
            f"Winners         : {winners}"
        )

        print(
            f"Losers          : {losers}"
        )

        print(
            f"Win Rate        : {win_rate:.2f}%"
        )

        print()

        print(
            f"Average Win     : ${average_win:.2f}"
        )

        print(
            f"Average Loss    : ${average_loss:.2f}"
        )

        print(
            f"Max Drawdown    : {max_drawdown:.2f}%"
        )

        print("=====================================\n")