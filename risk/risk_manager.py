from risk.stop_loss import StopLoss
from risk.take_profit import TakeProfit
from risk.trailing_stop import TrailingStop
from risk.break_even import BreakEven


class RiskManager:

    def __init__(self, execution_engine):

        self.execution = execution_engine

    def update_highest_price(self, row):

        self.execution.portfolio.highest_price = max(
            self.execution.portfolio.highest_price,
            row["high"]
        )

    def process(self, row):

        if not self.execution.portfolio.in_position():
            return

        old_high = self.execution.portfolio.highest_price

        self.update_highest_price(row)

        if self.execution.portfolio.highest_price > old_high:
            self.check_trailing_stop()

        self.check_break_even()

        self.check_stop_loss(row)

        if not self.execution.portfolio.in_position():
            return

        self.check_take_profit(row)

    def check_stop_loss(self, row):

        if StopLoss.is_triggered(
            current_low=row["low"],
            stop_price=self.execution.portfolio.stop_price
        ):

            print("\n========== STOP LOSS ==========")
            print(f"Market Low : {row['low']:.2f}")
            print(f"Stop Price : {self.execution.portfolio.stop_price:.2f}")
            print("===============================\n")

            self.execution.sell(
                timestamp=row["timestamp"],
                price=self.execution.portfolio.stop_price,
                exit_reason="Stop Loss"
            )

    def check_take_profit(self, row):

        if TakeProfit.is_triggered(
            current_high=row["high"],
            take_profit_price=self.execution.portfolio.take_profit_price
        ):

            print("\n========== TAKE PROFIT ==========")
            print(f"Market High : {row['high']:.2f}")
            print(f"Target Price: {self.execution.portfolio.take_profit_price:.2f}")
            print("=================================\n")

            self.execution.sell(
                timestamp=row["timestamp"],
                price=self.execution.portfolio.take_profit_price,
                exit_reason="Take Profit"
            )
    def check_trailing_stop(self):

        portfolio = self.execution.portfolio
        if not portfolio.break_even_active:
            return

        new_stop = TrailingStop.calculate(
            current_high=portfolio.highest_price,
            current_stop=portfolio.stop_price,
            trailing_percent=self.execution.settings.trailing_stop_percent
        )

        if new_stop > portfolio.stop_price:

            print("\n========== TRAILING STOP ==========")
            print(f"Highest Price : {portfolio.highest_price:.2f}")
            print(f"Old Stop      : {portfolio.stop_price:.2f}")
            print(f"New Stop      : {new_stop:.2f}")
            print("===================================\n")

            portfolio.stop_price = new_stop
    def check_break_even(self):

        portfolio = self.execution.portfolio

        if portfolio.break_even_active:
            return

        if BreakEven.should_activate(
            entry_price=portfolio.entry_price,
            highest_price=portfolio.highest_price,
            trigger_percent=self.execution.settings.break_even_trigger_percent
        ):

            portfolio.stop_price = portfolio.entry_price

            portfolio.break_even_active = True

            print("\n========== BREAK EVEN ==========")
            print(f"Entry Price : {portfolio.entry_price:.2f}")
            print(f"New Stop    : {portfolio.stop_price:.2f}")
            print("================================\n")