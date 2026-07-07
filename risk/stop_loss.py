class StopLoss:

    @staticmethod
    def percentage(
        entry_price: float,
        stop_percent: float
    ):

        return entry_price * (1 - stop_percent)