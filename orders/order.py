from abc import ABC
from dataclasses import dataclass
from datetime import datetime

from orders.order_status import OrderStatus


@dataclass
class Order(ABC):

    symbol: str

    side: str

    quantity: float

    timestamp: datetime

    status: OrderStatus = OrderStatus.PENDING

    filled_price: float | None = None

    filled_time: datetime | None = None