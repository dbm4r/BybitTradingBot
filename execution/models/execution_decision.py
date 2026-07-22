from dataclasses import dataclass

from risk.models.risk_decision import (
    RiskDecision,
)


@dataclass(
    slots=True,
)
class ExecutionDecision:

    approved: bool

    risk_decision: RiskDecision

    reason: str | None = None

    @classmethod
    def approve(
        cls,
        risk_decision: RiskDecision,
    ):

        return cls(
            approved=True,
            risk_decision=risk_decision,
        )

    @classmethod
    def reject(
        cls,
        risk_decision: RiskDecision,
        reason: str,
    ):

        return cls(
            approved=False,
            risk_decision=risk_decision,
            reason=reason,
        )