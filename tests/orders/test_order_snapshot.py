from datetime import datetime
from dataclasses import FrozenInstanceError

import pytest

from orders.lifecycle.order_state import (
    OrderState,
)

from orders.market_order import (
    MarketOrder,
)

from orders.models.order_snapshot import (
    OrderSnapshot,
)


def test_snapshot_contains_order_data():

    order = MarketOrder(
        symbol="BTCUSDT",
        side="BUY",
        quantity=2,
        timestamp=datetime.now(),
    )

    snapshot = OrderSnapshot(
        symbol=order.symbol,
        side=order.side,
        quantity=order.quantity,
        timestamp=order.timestamp,
        order_type=order.order_type,
        status=order.status,
        exchange_order_id=order.exchange_order_id,
        filled_price=order.filled_price,
        filled_time=order.filled_time,
        filled_quantity=order.filled_quantity,
        remaining_quantity=order.remaining_quantity,
    )

    assert snapshot.symbol == order.symbol

    assert snapshot.side == order.side

    assert snapshot.quantity == order.quantity

    assert snapshot.status == OrderState.CREATED


def test_snapshot_is_immutable():

    snapshot = OrderSnapshot(
        symbol="BTCUSDT",
        side="BUY",
        quantity=1,
        timestamp=datetime.now(),
        order_type=MarketOrder.order_type,
        status=OrderState.CREATED,
        exchange_order_id=None,
        filled_price=None,
        filled_time=None,
        filled_quantity=0,
        remaining_quantity=1,
    )

    with pytest.raises(
        FrozenInstanceError,
    ):

        snapshot.quantity = 10