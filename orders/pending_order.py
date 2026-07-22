from dataclasses import dataclass
from datetime import datetime

from orders.lifecycle.order_lifecycle_manager import (
    OrderLifecycleManager,
)

from orders.lifecycle.order_state import (
    OrderState,
)

from orders.order import (
    Order,
)

from orders.time_in_force import (
    TimeInForce,
)


@dataclass
class PendingOrder(Order):

    time_in_force: TimeInForce = (
        TimeInForce.GTC
    )

    expires_at: datetime | None = None

    def cancel(
        self,
    ):

        OrderLifecycleManager.transition(
            self,
            OrderState.CANCELLED,
        )

    def expire(
        self,
    ):

        OrderLifecycleManager.transition(
            self,
            OrderState.EXPIRED,
        )

    @property
    def active(
        self,
    ):

        return OrderLifecycleManager.is_active(
            self,
        )