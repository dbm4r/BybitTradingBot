from datetime import datetime

from orders.models.fill import (
    Fill,
)


def test_fill():

    now = datetime.now()

    fill = Fill(
        quantity=1,
        price=100,
        timestamp=now,
        fee=0.1,
    )

    assert fill.quantity == 1

    assert fill.price == 100

    assert fill.timestamp == now

    assert fill.fee == 0.1