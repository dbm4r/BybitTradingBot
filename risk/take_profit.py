class TakeProfit:

    @staticmethod
    def percentage(
        entry_price: float,
        take_profit_percent: float
    ) -> float:
        """
        Calculate the take-profit price.
        """
        return entry_price * (1 + take_profit_percent)

    @staticmethod
    def is_triggered(
        current_high: float,
        take_profit_price: float
    ) -> bool:
        """
        Check whether the take-profit target was reached.
        """
        return current_high >= take_profit_price