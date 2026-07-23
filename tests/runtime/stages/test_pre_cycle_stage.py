from unittest.mock import Mock

from runtime.cycle.stages.pre_cycle_stage import (
    PreCycleStage,
)


def test_pre_cycle_stage_returns_context():

    context = Mock()

    stage = PreCycleStage()

    result = stage.execute(
        context,
    )

    assert result is context