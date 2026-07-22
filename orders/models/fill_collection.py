from orders.models.fill import (
    Fill,
)


class FillCollection:

    def __init__(
        self,
    ):

        self._fills = []

    def append(
        self,
        fill: Fill,
    ):

        self._fills.append(
            fill,
        )

    @property
    def fills(
        self,
    ):

        return tuple(
            self._fills,
        )

    @property
    def last(
        self,
    ):

        if not self._fills:

            return None

        return self._fills[-1]

    @property
    def total_quantity(
        self,
    ):

        return sum(
            fill.quantity
            for fill in self._fills
        )

    @property
    def total_fee(
        self,
    ):

        return sum(
            fill.fee
            for fill in self._fills
        )

    @property
    def average_price(
        self,
    ):

        quantity = self.total_quantity

        if quantity == 0:

            return 0.0

        value = sum(
            fill.price * fill.quantity
            for fill in self._fills
        )

        return value / quantity

    def clear(
        self,
    ):

        self._fills.clear()