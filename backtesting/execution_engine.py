from backtesting.trade import Trade
from config import TRADING_FEE


class ExecutionEngine:

    def __init__(self, portfolio):

        self.portfolio = portfolio
        self.trades = []
        self.total_fees = 0
    
    def buy(self, timestamp, price):

        fee = self.portfolio.cash * TRADING_FEE

        cash_after_fee = self.portfolio.cash - fee

        quantity = cash_after_fee / price

        self.total_fees += fee

        self.portfolio.position = quantity
        self.portfolio.cash = 0

        self.portfolio.entry_price = price
        self.portfolio.entry_time = timestamp
    def sell(self, timestamp, price):

        gross_exit_value = self.portfolio.position * price

        fee = gross_exit_value * TRADING_FEE

        exit_value = gross_exit_value - fee

        self.total_fees += fee

        entry_value = (
            self.portfolio.position
            * self.portfolio.entry_price
        )

        gross_profit = gross_exit_value - entry_value

        net_profit = gross_profit - fee

        duration = (
            timestamp - self.portfolio.entry_time
        ).total_seconds() / 3600

        trade = Trade(
            symbol="BTCUSDT",
            strategy="SMA Crossover",

            entry_time=self.portfolio.entry_time,
            exit_time=timestamp,

            entry_price=self.portfolio.entry_price,
            exit_price=price,

            quantity=self.portfolio.position,

            gross_profit=gross_profit,
            fees=fee,
            net_profit=net_profit,

            profit_percent=(net_profit / entry_value) * 100,

            duration=duration
        )

        self.trades.append(trade)

        self.portfolio.cash = exit_value

        self.portfolio.position = 0

        self.portfolio.entry_price = None
        self.portfolio.entry_time = None
    def process_signal(self, signal, timestamp, price):

        if signal == 1 and not self.portfolio.in_position():

            self.buy(timestamp, price)

        elif signal == -1 and self.portfolio.in_position():

            self.sell(timestamp, price)