from datetime import datetime

from orders.events.order_event import (
    OrderEvent,
)

from orders.history.order_history import (
    OrderHistory,
)

from orders.lifecycle.order_state import (
    OrderState,
)


def test_append_event():

    history = OrderHistory()

    event = OrderEvent(
        state=OrderState.CREATED,
        timestamp=datetime.now(),
    )

    history.append(
        event,
    )

    assert len(
        history.events
    ) == 1

    assert (
        history.last
        == event
    )


def test_clear_history():

    history = OrderHistory()

    history.append(
        OrderEvent(
            state=OrderState.CREATED,
            timestamp=datetime.now(),
        )
    )

    history.clear()

    assert len(
        history.events
    ) == 0