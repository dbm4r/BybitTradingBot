from datetime import datetime

from events.event_bus import (
    EventBus,
)

from orders.lifecycle.order_lifecycle_manager import (
    OrderLifecycleManager,
)

from orders.lifecycle.order_state import (
    OrderState,
)

from orders.market_order import (
    MarketOrder,
)

from orders.models.fill import (
    Fill,
)

from orders.order_manager import (
    OrderManager,
)


class DummyEngine:

    def __init__(
        self,
    ):

        self.events = EventBus()


def create_order(
    quantity,
):

    order = MarketOrder(
        symbol="BTCUSDT",
        side="BUY",
        quantity=quantity,
        timestamp=datetime.now(),
    )

    OrderLifecycleManager.transition(
        order,
        OrderState.SUBMITTED,
    )

    OrderLifecycleManager.transition(
        order,
        OrderState.ACCEPTED,
    )

    return order


def test_fill_is_added_to_collection():

    engine = DummyEngine()

    manager = OrderManager()

    order = create_order(
        quantity=2,
    )

    fill = Fill(
        quantity=1,
        price=100,
        timestamp=datetime.now(),
    )

    manager.fill(
        engine=engine,
        order=order,
        fill=fill,
    )

    assert len(
        order.fills.fills
    ) == 1

    assert (
        order.fills.last
        == fill
    )

    assert (
        order.fills.total_quantity
        == 1
    )

    assert (
        order.remaining_quantity
        == 1
    )

    assert (
        order.filled_quantity
        == 1
    )

    assert (
        order.status
        == OrderState.PARTIALLY_FILLED
    )


def test_multiple_fills_are_recorded():

    engine = DummyEngine()

    manager = OrderManager()

    order = create_order(
        quantity=3,
    )

    manager.fill(
        engine=engine,
        order=order,
        fill=Fill(
            quantity=1,
            price=100,
            timestamp=datetime.now(),
        ),
    )

    manager.fill(
        engine=engine,
        order=order,
        fill=Fill(
            quantity=2,
            price=110,
            timestamp=datetime.now(),
        ),
    )

    assert len(
        order.fills.fills
    ) == 2

    assert (
        order.fills.total_quantity
        == 3
    )

    assert (
        order.fills.average_price
        == (100 * 1 + 110 * 2) / 3
    )

    assert (
        order.remaining_quantity
        == 0
    )

    assert (
        order.filled_quantity
        == 3
    )

    assert (
        order.status
        == OrderState.FILLED
    )