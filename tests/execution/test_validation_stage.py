from execution.framework.stages.validation_stage import (
    ValidationStage,
)

from tests.execution.test_order_validation_service import (
    DummyEngine,
    create_context,
)


def test_validation_stage():

    context = (
        ValidationStage().execute(
            DummyEngine(),
            create_context(),
        )
    )

    assert context.position_size.quantity > 0