from execution.framework.base_executor import (
    BaseExecutor,
)

from execution.services.exit_order_request_factory import (
    ExitOrderRequestFactory,
)


class ExitOrderCreationStage(
    BaseExecutor,
):

    def execute(
        self,
        engine,
        context,
    ):

        context.order = (
            ExitOrderRequestFactory.create(
                engine=engine,
                context=context,
                timestamp=context.timestamp,
            )
        )

        return context