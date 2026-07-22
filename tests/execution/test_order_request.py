from datetime import UTC, datetime

from execution.models.order_request import (
    OrderRequest,
)


def test_order_request():

    request = OrderRequest(
        symbol="BTCUSDT",
        side="BUY",
        quantity=1,
        price=100,
        timestamp=datetime.now(UTC),
    )

    assert request.symbol == "BTCUSDT"

    assert request.side == "BUY"

    assert request.order_type == "MARKET"