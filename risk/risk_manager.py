from risk.stop_loss import StopLoss
from risk.take_profit import TakeProfit
from risk.trailing_stop import TrailingStop
from risk.break_even import BreakEven


class RiskManager:

    def __init__(self, execution_engine):

        self.execution = execution_engine

    def update_highest_price(
        self,
        position,
        row
    ):

        position.highest_price = max(
            position.highest_price,
            row["high"]
        )

    def process(self, row):

        position = self.execution.portfolio.get_position(
            self.execution.symbol
        )

        if not position.is_open():
            return

        old_high = position.highest_price

        self.update_highest_price(
            position,
            row
        )

        made_new_high = (
            position.highest_price > old_high
        )

        self.check_break_even(position)

        self.check_trailing_activation(position)

        if made_new_high:
            self.check_trailing_stop(position)

        self.check_stop_loss(
            position,
            row
        )

        if not position.is_open():
            return

        self.check_take_profit(
            position,
            row
        )

    def check_stop_loss(
        self,
        position,
        row
    ):

        if StopLoss.is_triggered(
            current_low=row["low"],
            stop_price=position.stop_price
        ):

            print("\n========== STOP LOSS ==========")
            print(f"Market Low : {row['low']:.2f}")
            print(f"Stop Price : {position.stop_price:.2f}")
            print("===============================\n")

            self.execution.sell(
                timestamp=row["timestamp"],
                price=position.stop_price,
                exit_reason="Stop Loss"
            )

    def check_take_profit(
        self,
        position,
        row
    ):

        if TakeProfit.is_triggered(
            current_high=row["high"],
            take_profit_price=position.take_profit_price
        ):

            print("\n========== TAKE PROFIT ==========")
            print(f"Market High : {row['high']:.2f}")
            print(f"Target Price: {position.take_profit_price:.2f}")
            print("=================================\n")

            self.execution.sell(
                timestamp=row["timestamp"],
                price=position.take_profit_price,
                exit_reason="Take Profit"
            )
    def check_trailing_stop(
        self,
        position
    ):

        if not position.trailing_active:
            return

        new_stop = TrailingStop.calculate(
            current_high=position.highest_price,
            current_stop=position.stop_price,
            trailing_percent=self.execution.settings.trailing_stop_percent
        )

        if new_stop <= position.stop_price:
            return

        print("\n========== TRAILING STOP ==========")
        print(f"Highest Price : {position.highest_price:.2f}")
        print(f"Old Stop      : {position.stop_price:.2f}")
        print(f"New Stop      : {new_stop:.2f}")
        print("===================================\n")

        position.stop_price = new_stop
    def check_break_even(
        self,
        position
    ):

        if position.break_even_active:
            return

        if BreakEven.should_activate(
            entry_price=position.entry_price,
            highest_price=position.highest_price,
            trigger_percent=self.execution.settings.break_even_trigger_percent
        ):

            position.stop_price = position.entry_price

            position.break_even_active = True

            print("\n========== BREAK EVEN ==========")
            print(f"Entry Price : {position.entry_price:.2f}")
            print(f"New Stop    : {position.stop_price:.2f}")
            print("================================\n")
    
    def check_trailing_activation(
        self,
        position
    ):

        if position.trailing_active:
            return

        if TrailingStop.should_activate(
            entry_price=position.entry_price,
            highest_price=position.highest_price,
            trigger_percent=self.execution.settings.trailing_activation_percent
        ):

            position.trailing_active = True

            print("\n====== TRAILING ACTIVATED ======")
            print(f"Highest Price : {position.highest_price:.2f}")
            print("Trailing Stop Enabled")
            print("================================\n")