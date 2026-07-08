from abc import ABC
from dataclasses import dataclass
from orders.order_status import OrderStatus
from orders.order import Order
from orders.time_in_force import TimeInForce
from datetime import datetime




@dataclass
class PendingOrder(Order):

    time_in_force: TimeInForce = TimeInForce.GTC

    expires_at: datetime | None = None

    def cancel(self):

        self.status = OrderStatus.CANCELLED

    def expire(self):

        self.status = OrderStatus.EXPIRED

    @property
    def active(self):

        return self.status == OrderStatus.PENDING