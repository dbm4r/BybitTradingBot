from strategies.sma_crossover import SMACrossoverStrategy


class StrategyFactory:

    _strategies = {
        "SMA": SMACrossoverStrategy,
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

        return cls._strategies[name](**kwargs)