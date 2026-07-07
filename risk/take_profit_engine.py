class TakeProfitEngine:

    @staticmethod
    def is_triggered(
        current_high: float,
        take_profit_price: float
    ) -> bool:

        return current_high >= take_profit_price