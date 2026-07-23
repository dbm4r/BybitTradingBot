from runtime.cycle.framework.trading_cycle_pipeline import (
    TradingCyclePipeline,
)

from runtime.cycle.stages.post_cycle_stage import (
    PostCycleStage,
)

from runtime.cycle.stages.pre_cycle_stage import (
    PreCycleStage,
)

from runtime.cycle.stages.process_stage import (
    ProcessStage,
)

from runtime.cycle.stages.scan_stage import (
    ScanStage,
)


class TradingCyclePipelineBuilder:

    def __init__(
        self,
    ):

        self._stages = []

    def add_stage(
        self,
        stage,
    ):

        self._stages.append(
            stage,
        )

        return self

    def default_pipeline(
        self,
    ):

        return (
            self.add_stage(
                PreCycleStage(),
            )
            .add_stage(
                ScanStage(),
            )
            .add_stage(
                ProcessStage(),
            )
            .add_stage(
                PostCycleStage(),
            )
        )

    def build(
        self,
    ):

        return TradingCyclePipeline(
            self._stages,
        )