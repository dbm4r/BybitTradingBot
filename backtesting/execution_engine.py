from risk.risk_manager import RiskManager
from orders.order_manager import OrderManager
from execution.entry_executor import EntryExecutor
from execution.exit_executor import ExitExecutor




class ExecutionEngine:

    def __init__(self, portfolio, settings, symbol, strategy_name):

        self.portfolio = portfolio
        self.settings = settings

        self.symbol = symbol
        self.strategy_name = strategy_name

        self.trades = []
        self.total_fees = 0
        self.risk_manager = RiskManager(self)
        self.order_manager = OrderManager()
    
    def buy(self, timestamp, price) -> None:

        EntryExecutor.execute(
            engine=self,
            timestamp=timestamp,
            price=price)

    def sell(
            self, timestamp, price, exit_reason) -> None:

        ExitExecutor.execute(
            engine=self,
            timestamp=timestamp,
            price=price,
            exit_reason=exit_reason
        )
    def process_candle(self, row):

        # First check if an open trade should be closed by the stop loss
        self.risk_manager.process(row)

        signal = row["signal"]
        timestamp = row["timestamp"]
        price = row["close"]

        # Buy signal
        if signal == 1 and not self.portfolio.in_position():

            self.buy(timestamp, price)

        # Sell signal
        elif signal == -1 and self.portfolio.in_position():

            self.sell(
                timestamp,
                price,
                "Signal"
            )