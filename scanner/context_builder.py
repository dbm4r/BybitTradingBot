from market.multi_timeframe_context import (
    MultiTimeframeContext,
)
from market.timeframe_context import (
    TimeframeContext,
)


class ContextBuilder:

    @staticmethod
    def build(
        candle_series,
    ) -> MultiTimeframeContext:

        context = TimeframeContext(
            timeframe=candle_series.interval,
            candles=candle_series,
        )

        return MultiTimeframeContext(
            contexts={
                candle_series.interval: context,
            }
        )