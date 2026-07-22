from dataclasses import dataclass



@dataclass
class OCOManager:

    def __init__(self):

        self.groups = []

    def add(self, group):

        self.groups.append(group)
    def on_order_filled(
        self,
        order,
        order_manager
    ):

        for group in self.groups:

            if order not in group.orders():
                continue

            other = (
                group.second
                if group.first == order
                else group.first
            )

            if other.active:

                order_manager.cancel(other)