from execution.execution_state import (
    ExecutionState,
)


class DummyOrder:

    def __init__(
        self,
        order_id,
    ):

        self.exchange_order_id = order_id


def test_register_pending_order():

    state = ExecutionState()

    order = DummyOrder(
        "order-1",
    )

    state.register_pending_order(
        order,
    )

    assert state.has_pending_order(
        "order-1",
    )


def test_get_pending_order():

    state = ExecutionState()

    order = DummyOrder(
        "order-1",
    )

    state.register_pending_order(
        order,
    )

    assert (
        state.get_pending_order(
            "order-1",
        )
        is order
    )


def test_unregister_pending_order():

    state = ExecutionState()

    order = DummyOrder(
        "order-1",
    )

    state.register_pending_order(
        order,
    )

    removed = state.unregister_pending_order(
        "order-1",
    )

    assert removed is order

    assert not state.has_pending_order(
        "order-1",
    )


def test_pending_orders():

    state = ExecutionState()

    order1 = DummyOrder(
        "order-1",
    )

    order2 = DummyOrder(
        "order-2",
    )

    state.register_pending_order(
        order1,
    )

    state.register_pending_order(
        order2,
    )

    orders = state.pending_orders()

    assert len(
        orders,
    ) == 2

    assert order1 in orders

    assert order2 in orders


def test_clear_pending_orders():

    state = ExecutionState()

    state.register_pending_order(
        DummyOrder(
            "order-1",
        ),
    )

    state.register_pending_order(
        DummyOrder(
            "order-2",
        ),
    )

    state.clear_pending_orders()

    assert (
        len(
            state.pending_orders(),
        )
        == 0
    )


def test_get_unknown_pending_order_returns_none():

    state = ExecutionState()

    assert (
        state.get_pending_order(
            "unknown",
        )
        is None
    )


def test_unregister_unknown_pending_order_returns_none():

    state = ExecutionState()

    assert (
        state.unregister_pending_order(
            "unknown",
        )
        is None
    )


def test_has_pending_order_returns_false_for_unknown_order():

    state = ExecutionState()

    assert not state.has_pending_order(
        "unknown",
    )