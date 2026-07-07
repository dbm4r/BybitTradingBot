class BreakEven:

    @staticmethod
    def should_activate(
        entry_price: float,
        highest_price: float,
        trigger_percent: float
    ) -> bool:

        trigger_price = entry_price * (1 + trigger_percent)

        return highest_price >= trigger_price