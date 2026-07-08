from dataclasses import dataclass, field

from orders.pending_order import PendingOrder
from orders.order_type import OrderType


@dataclass
class StopLimitOrder(PendingOrder):

    order_type: OrderType = field(
        default=OrderType.STOP_LIMIT,
        init=False
    )

    stop_price: float = 0

    limit_price: float = 0

    triggered: bool = False

    @property
    def execution_price(self):

        return self.limit_price

    def should_fill(self, row):

        if not self.triggered:

            if self.side == "BUY":

                self.triggered = (
                    row["high"] >= self.stop_price
                )

            else:

                self.triggered = (
                    row["low"] <= self.stop_price
                )

        if not self.triggered:
            return False

        if self.side == "BUY":

            return row["low"] <= self.limit_price

        return row["high"] >= self.limit_price