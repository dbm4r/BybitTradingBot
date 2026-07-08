from dataclasses import dataclass, field

from orders.order import Order
from orders.order_type import OrderType


@dataclass
class MarketOrder(Order):

    order_type: OrderType = field(
        default=OrderType.MARKET,
        init=False
    )

    @property
    def execution_price(self):

        return self.filled_price

    def should_fill(self, row):

        return True