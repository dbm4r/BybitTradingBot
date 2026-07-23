from unittest.mock import Mock

from runtime.cycle.stages.process_stage import (
    ProcessStage,
)


def test_process_stage_processes_opportunities():

    opportunities = [
        Mock(),
        Mock(),
    ]

    context = Mock()

    context.opportunities = opportunities

    stage = ProcessStage()

    result = stage.execute(
        context,
    )

    context.processor.process.assert_called_once_with(
        opportunities,
    )

    assert result is context