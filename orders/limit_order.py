from dataclasses import dataclass, field

from orders.pending_order import PendingOrder
from orders.order_type import OrderType


@dataclass
class LimitOrder(PendingOrder):

    order_type: OrderType = field(
        default=OrderType.LIMIT,
        init=False
    )

    limit_price: float = 0
    @property
    def execution_price(self):

        return self.limit_price

    def should_fill(self, row):

        if self.side == "BUY":
            return row["low"] <= self.limit_price

        return row["high"] >= self.limit_price