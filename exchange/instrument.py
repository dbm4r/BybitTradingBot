from dataclasses import dataclass
import math


@dataclass
class Instrument:

    symbol: str

    qty_step: float
    min_qty: float
    max_qty: float

    tick_size: float

    def round_quantity(
        self,
        quantity
    ):

        return (
            math.floor(
                quantity / self.qty_step
            ) * self.qty_step
        )

    def round_price(
        self,
        price
    ):

        return (
            round(
                price / self.tick_size
            ) * self.tick_size
        )

    def validate_quantity(
        self,
        quantity
    ):

        return (
            self.min_qty
            <= quantity
            <= self.max_qty
        )