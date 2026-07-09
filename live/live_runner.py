from live.scheduler import Scheduler
from live.candle_provider import CandleProvider


class LiveRunner:

    def __init__(
        self,
        client,
        strategy,
        execution_engine,
        symbol,
        interval=1
    ):

        self.provider = CandleProvider(client)
        self.strategy = strategy
        self.engine = execution_engine
        self.symbol = symbol
        self.interval = interval

    def run(self):

        print("Live Runner Started")

        try:

            while True:

                Scheduler.wait_for_next_candle(
                    self.interval
                )

                dataframe = self.provider.recent_candles(
                    symbol=self.symbol,
                    interval=str(self.interval),
                    limit=200
                )

                dataframe = self.strategy.generate_signals(
                    dataframe
                )

                row = dataframe.iloc[-1]

                print("\n========== LIVE SIGNAL ==========")
                print(f"Time   : {row['timestamp']}")
                print(f"Price  : {row['close']}")
                print(f"Signal : {row['signal']}")
                print("=================================")

        except KeyboardInterrupt:

            print("\nStopping Live Runner...")