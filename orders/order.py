from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from dataclasses import field
from datetime import datetime

from orders.history.order_history import (
    OrderHistory,
)

from orders.lifecycle.order_lifecycle_manager import (
    OrderLifecycleManager,
)

from orders.lifecycle.order_state import (
    OrderState,
)

from orders.models.fill_collection import (
    FillCollection,
)

from orders.models.order_snapshot import (
    OrderSnapshot,
)

from orders.order_type import (
    OrderType,
)


@dataclass
class Order(ABC):

    symbol: str

    side: str

    quantity: float

    timestamp: datetime

    order_type: OrderType

    status: OrderState = OrderState.CREATED

    history: OrderHistory = field(
        init=False,
    )

    fills: FillCollection = field(
        init=False,
    )

    exchange_order_id: str | None = None

    filled_price: float | None = None

    filled_time: datetime | None = None

    filled_quantity: float = 0

    remaining_quantity: float = 0

    def __post_init__(
        self,
    ):

        self.remaining_quantity = (
            self.quantity
        )

        self.history = OrderHistory()

        self.fills = FillCollection()

        OrderLifecycleManager.initialize(
            self,
        )

    @abstractmethod
    def should_fill(
        self,
        row,
    ) -> bool:
        pass

    @property
    @abstractmethod
    def execution_price(
        self,
    ):
        pass

    def snapshot(
        self,
    ) -> OrderSnapshot:

        return OrderSnapshot(
            symbol=self.symbol,
            side=self.side,
            quantity=self.quantity,
            timestamp=self.timestamp,
            order_type=self.order_type,
            status=self.status,
            exchange_order_id=self.exchange_order_id,
            filled_price=self.filled_price,
            filled_time=self.filled_time,
            filled_quantity=self.filled_quantity,
            remaining_quantity=self.remaining_quantity,
        )