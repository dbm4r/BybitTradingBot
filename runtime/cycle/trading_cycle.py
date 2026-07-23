from runtime.cycle.framework.trading_cycle_pipeline import (
    TradingCyclePipeline,
)

from runtime.cycle.trading_context import (
    TradingContext,
)


class TradingCycle:

    def __init__(
        self,
        context: TradingContext,
        pipeline: TradingCyclePipeline,
    ):

        self._context = context
        self._pipeline = pipeline

    def run(
        self,
    ) -> None:

        self._pipeline.execute(
            self._context,
        )