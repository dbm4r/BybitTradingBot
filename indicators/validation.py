class IndicatorValidator:

    @staticmethod
    def validate_period(period: int) -> None:
        if period <= 0:
            raise ValueError(
                "Period must be greater than zero."
            )