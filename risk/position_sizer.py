class PositionSizer:

    @staticmethod
    def fixed_risk(
        account_balance: float,
        risk_percent: float,
        entry_price: float,
        stop_price: float
    ):

        risk_amount = account_balance * risk_percent

        risk_per_unit = entry_price - stop_price

        if risk_per_unit <= 0:
            return 0

        quantity = risk_amount / risk_per_unit

        return quantity