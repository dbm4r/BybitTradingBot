from backtesting.backtester import Backtester


class BacktestRunner:

    def __init__(
        self,
        settings,
        symbol,
    ):

        self.settings = settings
        self.symbol = symbol

    def run(
        self,
        dataframe,
        strategy,
    ):

        backtester = Backtester(
            settings=self.settings,
            symbol=self.symbol,
            strategy=strategy,
             interval="1"
        )

        trades = backtester.run(
            dataframe.copy(),
        )

        return backtester, trades