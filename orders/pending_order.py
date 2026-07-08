from abc import ABC
from dataclasses import dataclass

from orders.order import Order
from orders.time_in_force import TimeInForce


@dataclass
class PendingOrder(Order, ABC):

    time_in_force: TimeInForce = TimeInForce.GTC