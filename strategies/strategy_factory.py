from strategies.sma_crossover import SMACrossoverStrategy
from strategies.rsi_strategy import RSIStrategy


class StrategyFactory:

    _strategies = {
        "SMA": SMACrossoverStrategy,
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