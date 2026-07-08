from dataclasses import dataclass, field

from orders.pending_order import PendingOrder
from orders.order_type import OrderType


@dataclass
class StopOrder(PendingOrder):

    order_type: OrderType = field(
        default=OrderType.STOP,
        init=False
    )

    stop_price: float = 0
    @property
    def execution_price(self):

        return self.stop_price

    def should_fill(self, row):

        if self.side == "BUY":
            return row["high"] >= self.stop_price

        return row["low"] <= self.stop_price