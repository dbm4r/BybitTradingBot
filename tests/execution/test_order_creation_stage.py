from execution.framework.stages.order_creation_stage import (
    OrderCreationStage,
)

from tests.execution.test_order_request_factory import (
    DummyEngine,
    create_context,
)


def test_order_creation_stage():

    context = (
        OrderCreationStage().execute(
            DummyEngine(),
            create_context(),
        )
    )

    assert context.order is not None

    assert context.order.side == "BUY"