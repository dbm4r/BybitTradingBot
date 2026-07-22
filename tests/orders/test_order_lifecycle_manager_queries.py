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


def test_active_order():

    order = create_order()

    OrderLifecycleManager.transition(
        order,
        OrderState.SUBMITTED,
    )

    OrderLifecycleManager.transition(
        order,
        OrderState.ACCEPTED,
    )

    assert (
        OrderLifecycleManager.is_active(
            order,
        )
    )

    assert (
        OrderLifecycleManager.can_fill(
            order,
        )
    )

    assert (
        OrderLifecycleManager.can_cancel(
            order,
        )
    )

    assert not (
        OrderLifecycleManager.is_terminal(
            order,
        )
    )


def test_filled_order():

    order = create_order()

    OrderLifecycleManager.transition(
        order,
        OrderState.SUBMITTED,
    )

    OrderLifecycleManager.transition(
        order,
        OrderState.ACCEPTED,
    )

    OrderLifecycleManager.transition(
        order,
        OrderState.FILLED,
    )

    assert (
        OrderLifecycleManager.is_terminal(
            order,
        )
    )

    assert not (
        OrderLifecycleManager.is_active(
            order,
        )
    )

    assert not (
        OrderLifecycleManager.can_fill(
            order,
        )
    )

    assert not (
        OrderLifecycleManager.can_cancel(
            order,
        )
    )