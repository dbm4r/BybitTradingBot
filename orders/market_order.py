from dataclasses import dataclass
from orders.order import Order
from dataclasses import dataclass, field
from orders.order_type import OrderType


@dataclass
class MarketOrder(Order):

    order_type: OrderType = field(
        default=OrderType.MARKET,
        init=False
    )

    def should_fill(self, row):

        return True