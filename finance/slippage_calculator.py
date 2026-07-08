class SlippageCalculator:

    @staticmethod
    def apply_buy(
        price: float,
        slippage_percent: float
    ) -> float:

        return price * (
            1 + slippage_percent
        )

    @staticmethod
    def apply_sell(
        price: float,
        slippage_percent: float
    ) -> float:

        return price * (
            1 - slippage_percent
        )