class StopLossEngine:

    @staticmethod
    def is_triggered(
        current_low: float,
        stop_price: float
    ) -> bool:

        return current_low <= stop_price