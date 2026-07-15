from indicators.sma import SimpleMovingAverage
from indicators.rsi import RelativeStrengthIndex
from indicators.ema import ExponentialMovingAverage
from indicators.base_indicator import BaseIndicator
from indicators.atr import AverageTrueRange
class IndicatorFactory:

    _registry: dict[str, type[BaseIndicator]] = {
        "SMA": SimpleMovingAverage,
        "EMA": ExponentialMovingAverage,
        "RSI": RelativeStrengthIndex,
        "ATR": AverageTrueRange,
    }
    
    @classmethod
    def register(
        cls,
        name: str,
        indicator: type[BaseIndicator],
    ) -> None:

        if not issubclass(indicator, BaseIndicator):
            raise TypeError(
                "Indicator must inherit from BaseIndicator."
            )

        if name in cls._registry:
            raise ValueError(
                f"Indicator '{name}' is already registered."
            )

        cls._registry[name] = indicator
    @classmethod
    def create(
        cls,
        name: str,
        **kwargs,
    ) -> BaseIndicator:

        indicator_class = cls._registry.get(name)

        if indicator_class is None:
            raise ValueError(
                f"Unknown indicator: {name}"
            )

        return indicator_class(**kwargs)