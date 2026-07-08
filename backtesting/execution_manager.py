from backtesting.execution_engine import ExecutionEngine



class ExecutionManager:

    def __init__(self, portfolio, settings):

        self.portfolio = portfolio
        self.settings = settings

        self.engines = {}

    def get_engine(
        self,
        symbol,
        strategy_name
    ):

        if symbol not in self.engines:

            self.engines[symbol] = ExecutionEngine(
                portfolio=self.portfolio,
                settings=self.settings,
                symbol=symbol,
                strategy_name=strategy_name
            )

        return self.engines[symbol]