from backtesting.backtester import Backtester


class BacktestRunner:

    def __init__(
        self,
        settings,
        symbol
    ):

        self.settings = settings
        self.symbol = symbol

    def run(
        self,
        dataframe,
        strategy
    ):

        dataframe = strategy.generate_signals(
            dataframe.copy()
        )

        backtester = Backtester(
            settings=self.settings,
            symbol=self.symbol,
            strategy=strategy
        )

        trades = backtester.run(
            dataframe
        )

        return backtester, trades