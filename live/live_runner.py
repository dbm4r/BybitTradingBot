from engine.engine_state import EngineState
from live.candle_provider import CandleProvider
from live.scheduler import Scheduler
from pipeline.trading_pipeline import TradingPipeline
from trading.trading_session import TradingSession


class LiveRunner:

    def __init__(
        self,
        client,
        strategy,
        execution_engine,
        symbol,
        interval=1,
    ):

        self.provider = CandleProvider(client)

        self.session = TradingSession(
            engine=execution_engine,
            pipeline=TradingPipeline(
                strategy=strategy,
                symbol=symbol,
                interval=str(interval),
            ),
        )

        self.engine = execution_engine
        self.symbol = symbol
        self.interval = interval

    def run(self):

        print("Live Runner Started")

        self.engine.state.set_state(
            EngineState.SYNCHRONIZING
        )

        history = self.provider.initialize(
            symbol=self.symbol,
            interval=str(self.interval),
            limit=200,
        )

        self.session.load_history(
            history
        )

        self.engine.state.set_state(
            EngineState.READY
        )

        try:

            while True:

                self.engine.state.set_state(
                    EngineState.WAITING_FOR_CANDLE
                )

                Scheduler.wait_for_next_candle(
                    self.interval
                )

                candle = self.provider.update(
                    symbol=self.symbol,
                    interval=str(self.interval),
                )

                if candle is None:
                    continue

                self.engine.state.set_state(
                    EngineState.GENERATING_SIGNAL
                )

                self.session.process_candle(
                    candle
                )

        except KeyboardInterrupt:

            self.engine.state.set_state(
                EngineState.STOPPED
            )

            print(
                "\nStopping Live Runner..."
            )

        except Exception:

            self.engine.state.set_state(
                EngineState.ERROR
            )

            raise