from dataclasses import dataclass
from datetime import datetime

from orders.lifecycle.order_state import (
    OrderState,
)


@dataclass(
    frozen=True,
    slots=True,
)
class OrderEvent:

    state: OrderState

    timestamp: datetime