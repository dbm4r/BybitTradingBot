from dataclasses import dataclass
from datetime import datetime

from orders.lifecycle.order_state import (
    OrderState,
)

from orders.order_type import (
    OrderType,
)


@dataclass(frozen=True)
class OrderSnapshot:

    symbol: str

    side: str

    quantity: float

    timestamp: datetime

    order_type: OrderType

    status: OrderState

    exchange_order_id: str | None

    filled_price: float | None

    filled_time: datetime | None

    filled_quantity: float

    remaining_quantity: float