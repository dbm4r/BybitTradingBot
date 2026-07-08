from indicators.moving_average import SimpleMovingAverage
from indicators.rsi import RelativeStrengthIndex


class IndicatorFactory:

    _indicators = {
        "SMA": SimpleMovingAverage,
        "RSI": RelativeStrengthIndex,
    }

    @classmethod
    def create(
        cls,
        name: str,
        **kwargs
    ):

        if name not in cls._indicators:

            raise ValueError(
                f"Unknown indicator: {name}"
            )

        return cls._indicators[name](**kwargs)