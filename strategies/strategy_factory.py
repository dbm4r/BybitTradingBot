from strategies.sma_crossover import SMACrossoverStrategy


class StrategyFactory:

    @staticmethod
    def create(name: str):

        strategies = {

            "SMA": SMACrossoverStrategy,

        }

        if name not in strategies:

            raise ValueError(
                f"Unknown strategy: {name}"
            )

        return strategies[name]()