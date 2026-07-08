class TrailingStop:


    @staticmethod
    def should_activate(
        entry_price: float,
        highest_price: float,
        trigger_percent: float
    ) -> bool:

        trigger_price = entry_price * (1 + trigger_percent)

        return highest_price >= trigger_price


    @staticmethod
    def calculate(
        current_high: float,
        current_stop: float,
        trailing_percent: float
    ) -> float:
        """
        Returns the new trailing stop.

        The stop can only move upward.
        """

        proposed_stop = current_high * (1 - trailing_percent)

        return max(current_stop, proposed_stop)