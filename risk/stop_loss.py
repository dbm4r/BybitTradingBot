class StopLoss:

    @staticmethod
    def percentage(
        entry_price: float,
        stop_percent: float
    ) -> float:
        """
        Calculate the stop-loss price.
        """
        return entry_price * (1 - stop_percent)

    @staticmethod
    def is_triggered(
        current_low: float,
        stop_price: float
    ) -> bool:
        """
        Check whether the stop-loss was hit.
        """
        return current_low <= stop_price