class TakeProfit:

    @staticmethod
    def percentage(
        entry_price: float,
        take_profit_percent: float
    ) -> float:

        return entry_price * (1 + take_profit_percent)