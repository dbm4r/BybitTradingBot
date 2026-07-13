from strategies.trend.sma_crossover import SMACrossoverStrategy
from strategies.momentum.ris import RSIStrategy
from strategies.trend.ema_crossover import EMACrossoverStrategy


class StrategyFactory:

    _strategies = {
        "SMA": SMACrossoverStrategy,
        "EMA": EMACrossoverStrategy,
        "RSI": RSIStrategy,
    }

    @classmethod
    def create(
        cls,
        name: str,
        **kwargs
    ):

        if name not in cls._strategies:

            raise ValueError(
                f"Unknown strategy: {name}"
            )

        strategy_class = cls._strategies[name]

        return strategy_class(**kwargs)