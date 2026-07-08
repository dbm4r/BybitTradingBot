from dataclasses import dataclass

from orders.pending_order import PendingOrder


@dataclass
class OCOOrder:

    first: PendingOrder

    second: PendingOrder

    def orders(self):

        return [
            self.first,
            self.second
        ]