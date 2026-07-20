from dataclasses import dataclass

from risk.models.risk_violation import (
    RiskViolation,
)


@dataclass(
    frozen=True,
    slots=True,
)
class RiskDecision:

    approved: bool

    quantity: float

    violations: tuple[RiskViolation, ...]

    reason: str

    @classmethod
    def approve(
        cls,
        quantity: float,
        reason: str = "Risk approved",
    ):

        return cls(
            approved=True,
            quantity=quantity,
            violations=(),
            reason=reason,
        )

    @classmethod
    def reject(
        cls,
        violations: tuple[RiskViolation, ...],
        reason: str = "Risk rejected",
    ):

        return cls(
            approved=False,
            quantity=0.0,
            violations=violations,
            reason=reason,
        )