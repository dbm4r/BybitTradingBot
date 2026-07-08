from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from orders.order_type import OrderType
from orders.order_status import OrderStatus


@dataclass
class Order(ABC):

    symbol: str
    side: str
    quantity: float
    timestamp: datetime
    order_type: OrderType

    status: OrderStatus = OrderStatus.PENDING

    filled_price: float | None = None
    filled_time: datetime | None = None
    filled_quantity: float = 0

    remaining_quantity: float = 0

    def __post_init__(self):

        self.remaining_quantity = self.quantity

    @abstractmethod
    def should_fill(self, row) -> bool:
        pass
    
    @property
    @abstractmethod
    def execution_price(self):
        pass
    
