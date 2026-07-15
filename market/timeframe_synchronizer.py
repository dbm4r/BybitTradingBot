from market.candle_aggregator import CandleAggregator
from market.multi_timeframe_context import MultiTimeframeContext
from market.timeframe import Timeframe
from market.timeframe_alignment import TimeframeAlignment
from market.timeframe_buffer import TimeframeBuffer
from models.candle import Candle


class TimeframeSynchronizer:

    def __init__(
        self,
        context: MultiTimeframeContext,
    ):

        self.context = context

        self.buffers = {
            Timeframe.M5: TimeframeBuffer(),
            Timeframe.M15: TimeframeBuffer(),
            Timeframe.H1: TimeframeBuffer(),
            Timeframe.H4: TimeframeBuffer(),
            Timeframe.D1: TimeframeBuffer(),
        }

    def update(
        self,
        candle: Candle,
    ) -> list[Candle]:

        created: list[Candle] = []

        for timeframe, buffer in self.buffers.items():

            bucket = TimeframeAlignment.align(
                candle.timestamp,
                timeframe,
            )

            if buffer.is_empty:

                buffer.start(bucket)

            elif buffer.bucket != bucket:

                aggregated = CandleAggregator.aggregate(
                    candles=buffer.candles,
                    interval=timeframe.value,
                )

                if timeframe.value in self.context.contexts:

                    timeframe_context = self.context.get(
                        timeframe.value
                    )

                    timeframe_context.candles.add(
                        aggregated
                    )

                    timeframe_context.calculate_indicators()

                created.append(
                    aggregated
                )

                buffer.start(bucket)

            buffer.add(candle)

        return created