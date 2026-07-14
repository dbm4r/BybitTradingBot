from backtesting.execution_engine import ExecutionEngine


class ExecutionManager:

    def __init__(self, portfolio, settings):

        self.portfolio = portfolio
        self.settings = settings

        self.engines = {}

    def get_engine(
        self,
        symbol,
        strategy
    ):

        key = (
            symbol,
            strategy.name,
            tuple(sorted(strategy.parameters.items()))
        )

        if key not in self.engines:

            self.engines[key] = ExecutionEngine(
                portfolio=self.portfolio,
                settings=self.settings,
                symbol=symbol,
                strategy=strategy,
                exchange_name="PAPER"
            )

        return self.engines[key]