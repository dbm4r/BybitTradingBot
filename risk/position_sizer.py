class PositionSizer:

    @staticmethod
    def fixed_risk(
        available_capital: float,
        risk_percent: float,
        entry_price: float,
        stop_price: float,
    ) -> float:

        risk_per_unit = abs(
            entry_price - stop_price
        )

        if risk_per_unit <= 0:
            return 0.0

        risk_amount = (
            available_capital
            * risk_percent
        )

        quantity = (
            risk_amount
            / risk_per_unit
        )

        return quantity