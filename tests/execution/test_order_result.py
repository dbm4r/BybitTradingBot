from datetime import UTC, datetime

from execution.models.order_result import (
    OrderResult,
)


def test_order_result():

    result = OrderResult(
        success=True,
        order_id="ABC123",
        quantity=2,
        price=100,
        fee=0.5,
        timestamp=datetime.now(UTC),
    )

    assert result.success

    assert result.order_id == "ABC123"

    assert result.quantity == 2