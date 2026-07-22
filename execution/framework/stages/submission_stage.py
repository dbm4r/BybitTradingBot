from execution.framework.base_executor import (
    BaseExecutor,
)

from execution.services.order_submission_service import (
    OrderSubmissionService,
)


class SubmissionStage(
    BaseExecutor,
):

    def execute(
        self,
        engine,
        context,
    ):

        context.exchange_result = (
            OrderSubmissionService.submit(
                engine=engine,
                order=context.order,
            )
        )

        return context