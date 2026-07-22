from datetime import datetime

from orders.models.fill import (
    Fill,
)

from orders.models.fill_collection import (
    FillCollection,
)


def test_append_fill():

    fills = FillCollection()

    fill = Fill(
        quantity=1,
        price=100,
        timestamp=datetime.now(),
        fee=0.1,
    )

    fills.append(
        fill,
    )

    assert len(
        fills.fills
    ) == 1

    assert (
        fills.last
        == fill
    )


def test_total_quantity():

    fills = FillCollection()

    fills.append(
        Fill(
            quantity=2,
            price=100,
            timestamp=datetime.now(),
        )
    )

    fills.append(
        Fill(
            quantity=3,
            price=110,
            timestamp=datetime.now(),
        )
    )

    assert (
        fills.total_quantity
        == 5
    )


def test_average_price():

    fills = FillCollection()

    fills.append(
        Fill(
            quantity=2,
            price=100,
            timestamp=datetime.now(),
        )
    )

    fills.append(
        Fill(
            quantity=3,
            price=110,
            timestamp=datetime.now(),
        )
    )

    assert (
        fills.average_price
        == 106
    )


def test_total_fee():

    fills = FillCollection()

    fills.append(
        Fill(
            quantity=1,
            price=100,
            timestamp=datetime.now(),
            fee=0.25,
        )
    )

    fills.append(
        Fill(
            quantity=1,
            price=100,
            timestamp=datetime.now(),
            fee=0.75,
        )
    )

    assert (
        fills.total_fee
        == 1.0
    )


def test_clear():

    fills = FillCollection()

    fills.append(
        Fill(
            quantity=1,
            price=100,
            timestamp=datetime.now(),
        )
    )

    fills.clear()

    assert len(
        fills.fills
    ) == 0