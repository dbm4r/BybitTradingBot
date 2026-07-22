from execution.models.execution_context import (
    ExecutionContext,
)

from execution.models.execution_decision import (
    ExecutionDecision,
)

from risk.models.exposure_snapshot import (
    ExposureSnapshot,
)

from risk.models.risk_budget import (
    RiskBudget,
)

from risk.models.risk_context import (
    RiskContext,
)


class RiskExecutionService:

    @staticmethod
    def evaluate(
        engine,
        context: ExecutionContext,
    ) -> ExecutionDecision:

        risk_context = RiskContext(
            decision=context.decision,
            position_size=context.position_size,
            portfolio=context.portfolio.portfolio,
            available_capital=context.available_capital,
            exposure=ExposureSnapshot(
                total_exposure=0,
                long_exposure=0,
                short_exposure=0,
                open_positions=0,
            ),
            budget=RiskBudget(
                total=0,
            ),
        )

        risk_decision = (
            engine.risk_engine.evaluate(
                risk_context,
            )
        )

        if risk_decision.approved:

            return ExecutionDecision.approve(
                risk_decision,
            )

        return ExecutionDecision.reject(
            risk_decision,
            risk_decision.reason,
        )