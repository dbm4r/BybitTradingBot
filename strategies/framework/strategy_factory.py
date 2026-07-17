from strategies.trend.sma_crossover import SMACrossover
from strategies.momentum.rsi import RSIStrategy
from strategies.trend.ema_crossover import EMACrossover


class StrategyFactory:

    _strategies = {
        "SMA": SMACrossover,
        "EMA": EMACrossover,
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