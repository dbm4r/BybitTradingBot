from orders.lifecycle.order_lifecycle_manager import (
    OrderLifecycleManager,
)

from orders.lifecycle.order_state import (
    OrderState,
)

from orders.market_order import (
    MarketOrder,
)


def create_order():

    return MarketOrder(
        symbol="BTCUSDT",
        side="BUY",
        quantity=1,
        timestamp=None,
    )


def test_initialize_creates_history():

    order = create_order()

    assert len(
        order.history.events
    ) == 1

    assert (
        order.history.last.state
        == OrderState.CREATED
    )


def test_transition_changes_order_state():

    order = create_order()

    OrderLifecycleManager.transition(
        order,
        OrderState.SUBMITTED,
    )

    assert (
        order.status
        == OrderState.SUBMITTED
    )

    assert len(
        order.history.events
    ) == 2

    assert (
        order.history.last.state
        == OrderState.SUBMITTED
    )


def test_invalid_transition_raises():

    order = create_order()

    try:

        OrderLifecycleManager.transition(
            order,
            OrderState.FILLED,
        )

        assert False

    except ValueError:

        assert True