from execution.framework.base_executor import (
    BaseExecutor,
)

from execution.services.order_validation_service import (
    OrderValidationService,
)


class ValidationStage(
    BaseExecutor,
):

    def execute(
        self,
        engine,
        context,
    ):

        context.position_size = (
            OrderValidationService.validate(
                engine=engine,
                context=context,
            )
        )

        return context