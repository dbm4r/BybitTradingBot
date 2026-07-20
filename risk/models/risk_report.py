from dataclasses import dataclass

from risk.models.risk_violation import (
    RiskViolation,
)


@dataclass(
    frozen=True,
    slots=True,
)
class RiskReport:

    passed_rules: tuple[str, ...]

    failed_rules: tuple[str, ...]

    violations: tuple[RiskViolation, ...]

    @property
    def approved(
        self,
    ) -> bool:

        return len(
            self.failed_rules
        ) == 0