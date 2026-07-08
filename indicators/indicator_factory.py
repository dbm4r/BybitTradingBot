from indicators.moving_average import SimpleMovingAverage
from indicators.rsi import RelativeStrengthIndex
from indicators.ema import ExponentialMovingAverage


class IndicatorFactory:

    _indicators = {
        "SMA": SimpleMovingAverage,
        "EMA": ExponentialMovingAverage,
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