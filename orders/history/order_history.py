from orders.events.order_event import (
    OrderEvent,
)


class OrderHistory:

    def __init__(
        self,
    ):

        self._events = []

    def append(
        self,
        event: OrderEvent,
    ):

        self._events.append(
            event,
        )

    @property
    def events(
        self,
    ):

        return tuple(
            self._events,
        )

    @property
    def last(
        self,
    ):

        if not self._events:

            return None

        return self._events[-1]

    def clear(
        self,
    ):

        self._events.clear()