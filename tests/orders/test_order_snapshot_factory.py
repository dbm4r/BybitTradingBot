from datetime import datetime

from orders.market_order import (
    MarketOrder,
)

from orders.models.order_snapshot import (
    OrderSnapshot,
)


def create_order():

    return MarketOrder(
        symbol="BTCUSDT",
        side="BUY",
        quantity=2,
        timestamp=datetime.now(),
    )


def test_snapshot_returns_snapshot():

    order = create_order()

    snapshot = order.snapshot()

    assert isinstance(
        snapshot,
        OrderSnapshot,
    )


def test_snapshot_contains_order_data():

    order = create_order()

    snapshot = order.snapshot()

    assert (
        snapshot.symbol
        == order.symbol
    )

    assert (
        snapshot.side
        == order.side
    )

    assert (
        snapshot.quantity
        == order.quantity
    )

    assert (
        snapshot.timestamp
        == order.timestamp
    )

    assert (
        snapshot.order_type
        == order.order_type
    )

    assert (
        snapshot.status
        == order.status
    )

    assert (
        snapshot.remaining_quantity
        == order.remaining_quantity
    )


def test_snapshot_returns_new_instance():

    order = create_order()

    snapshot1 = order.snapshot()

    snapshot2 = order.snapshot()

    assert snapshot1 is not snapshot2

    assert snapshot1 == snapshot2


def test_snapshot_does_not_change_after_order_changes():

    order = create_order()

    snapshot = order.snapshot()

    order.remaining_quantity = 1

    order.filled_quantity = 1

    assert (
        snapshot.remaining_quantity
        == 2
    )

    assert (
        snapshot.filled_quantity
        == 0
    )