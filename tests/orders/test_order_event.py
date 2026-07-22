from datetime import datetime

from orders.events.order_event import (
    OrderEvent,
)

from orders.lifecycle.order_state import (
    OrderState,
)


def test_order_event():

    now = datetime.now()

    event = OrderEvent(
        state=OrderState.CREATED,
        timestamp=now,
    )

    assert (
        event.state
        == OrderState.CREATED
    )

    assert (
        event.timestamp
        == now
    )