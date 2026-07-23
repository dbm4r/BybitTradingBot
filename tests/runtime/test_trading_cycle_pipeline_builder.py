from runtime.cycle.framework.trading_cycle_pipeline_builder import (
    TradingCyclePipelineBuilder,
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


def test_default_pipeline_contains_expected_stages():

    pipeline = (
        TradingCyclePipelineBuilder()
        .default_pipeline()
        .build()
    )

    stages = pipeline.stages

    assert len(stages) == 4

    assert isinstance(
        stages[0],
        PreCycleStage,
    )

    assert isinstance(
        stages[1],
        ScanStage,
    )

    assert isinstance(
        stages[2],
        ProcessStage,
    )

    assert isinstance(
        stages[3],
        PostCycleStage,
    )