from dataclasses import dataclass
from datetime import datetime
from portfolio.position_direction import PositionDirection


@dataclass
class Position:

    symbol: str

    quantity: float = 0

    entry_price: float | None = None

    entry_time: datetime | None = None

    stop_price: float | None = None

    take_profit_price: float | None = None

    highest_price: float | None = None

    break_even_active: bool = False
    trailing_active: bool = False
    direction: PositionDirection = PositionDirection.LONG
    def is_long(self):

        return self.direction == PositionDirection.LONG


    def is_short(self):

        return self.direction == PositionDirection.SHORT


    def is_open(self):

        return self.quantity > 0


    def close(self):

        self.quantity = 0

        self.entry_price = None
        self.entry_time = None

        self.stop_price = None
        self.take_profit_price = None

        self.highest_price = None

        self.break_even_active = False
        self.trailing_active = False
    def average_entry_price(
        self,
        current_quantity,
        current_price
    ):

        if self.entry_price is None:
            return current_price

        total_cost = (
            self.entry_price * self.quantity
            + current_price * current_quantity
        )

        total_quantity = (
            self.quantity + current_quantity
        )

        return total_cost / total_quantity