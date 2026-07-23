from unittest.mock import Mock

from runtime.cycle.stages.scan_stage import (
    ScanStage,
)


def test_scan_stage_stores_opportunities():

    opportunities = [
        Mock(),
        Mock(),
    ]

    context = Mock()

    context.scanner.scan.return_value = (
        opportunities
    )

    stage = ScanStage()

    result = stage.execute(
        context,
    )

    context.scanner.scan.assert_called_once_with()

    assert (
        context.opportunities
        == opportunities
    )

    assert result is context