from live.scheduler import Scheduler
from live.candle_provider import CandleProvider
from engine.engine_state import EngineState


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

        # Engine is starting synchronization
        self.engine.state.set_state(
            EngineState.SYNCHRONIZING
        )

        dataframe = self.provider.initialize(
            symbol=self.symbol,
            interval=str(self.interval),
            limit=200
        )

        # Initial synchronization finished
        self.engine.state.set_state(
            EngineState.READY
        )

        try:

            while True:

                # Waiting for next candle
                self.engine.state.set_state(
                    EngineState.WAITING_FOR_CANDLE
                )

                Scheduler.wait_for_next_candle(
                    self.interval
                )

                dataframe = self.provider.update(
                    symbol=self.symbol,
                    interval=str(self.interval)
                )

                if dataframe is None:
                    continue

                # Generating signals
                self.engine.state.set_state(
                    EngineState.GENERATING_SIGNAL
                )

                dataframe = self.strategy.generate_signals(
                    dataframe
                )

                row = dataframe.iloc[-1]

                self.engine.process_candle(row)

        except KeyboardInterrupt:

            self.engine.state.set_state(
                EngineState.STOPPED
            )

            print("\nStopping Live Runner...")

        except Exception:

            self.engine.state.set_state(
                EngineState.ERROR
            )

            raise