from execution.framework.base_executor import (
    BaseExecutor,
)

from execution.services.risk_execution_service import (
    RiskExecutionService,
)


class RiskStage(
    BaseExecutor,
):

    def execute(
        self,
        engine,
        context,
    ):

        context.risk_decision = (
            RiskExecutionService.evaluate(
                engine=engine,
                context=context,
            )
        )

        if not context.risk_decision.approved:

            context.continue_execution = False

            context.failure_reason = (
                context.risk_decision.reason
            )

        return context