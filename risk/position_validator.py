class PositionValidator:

    @staticmethod
    def validate(
        quantity: float,
        price: float,
        available_cash: float
    ):

        required_cash = quantity * price

        if required_cash <= available_cash:
            return quantity

        return available_cash / price