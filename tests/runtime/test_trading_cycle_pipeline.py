from unittest.mock import Mock

from runtime.cycle.framework.trading_cycle_pipeline import (
    TradingCyclePipeline,
)


def test_pipeline_executes_stages_in_order():

    context = Mock()

    stage1 = Mock()
    stage1.execute.return_value = context

    stage2 = Mock()
    stage2.execute.return_value = context

    pipeline = TradingCyclePipeline(
        [
            stage1,
            stage2,
        ]
    )

    result = pipeline.execute(
        context,
    )

    stage1.execute.assert_called_once_with(
        context,
    )

    stage2.execute.assert_called_once_with(
        context,
    )

    assert result is context