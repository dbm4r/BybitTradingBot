class TrailingStop:

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