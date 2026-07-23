from unittest.mock import Mock

from runtime.cycle.stages.post_cycle_stage import (
    PostCycleStage,
)


def test_post_cycle_stage_returns_context():

    context = Mock()

    stage = PostCycleStage()

    result = stage.execute(
        context,
    )

    assert result is context