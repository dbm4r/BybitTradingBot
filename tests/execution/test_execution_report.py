from datetime import UTC, datetime

from execution.models.execution_report import (
    ExecutionReport,
)

from execution.models.order_result import (
    OrderResult,
)


def test_execution_report():

    report = ExecutionReport(
        success=True,
        order=OrderResult(
            success=True,
            order_id="1",
            quantity=1,
            price=100,
            fee=0,
            timestamp=datetime.now(UTC),
        ),
    )

    assert report.success

    assert report.order.order_id == "1"