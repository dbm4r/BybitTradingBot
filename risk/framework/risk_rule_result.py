from dataclasses import dataclass

from risk.models.risk_violation import (
    RiskViolation,
)


@dataclass(
    frozen=True,
    slots=True,
)
class RiskRuleResult:

    passed: bool

    violations: tuple[RiskViolation, ...] = ()

    @classmethod
    def success(
        cls,
    ):

        return cls(
            passed=True,
        )

    @classmethod
    def failure(
        cls,
        *violations: RiskViolation,
    ):

        return cls(
            passed=False,
            violations=violations,
        )