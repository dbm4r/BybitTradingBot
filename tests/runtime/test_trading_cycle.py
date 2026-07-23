from unittest.mock import Mock

from runtime.cycle.trading_cycle import (
    TradingCycle,
)


def test_trading_cycle_runs_pipeline():

    context = Mock()

    pipeline = Mock()

    cycle = TradingCycle(
        context=context,
        pipeline=pipeline,
    )

    cycle.run()

    pipeline.execute.assert_called_once_with(
        context,
    )