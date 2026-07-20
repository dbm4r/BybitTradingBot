from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class RiskBudget:

    total: float

    used: float = 0.0

    @property
    def remaining(
        self,
    ) -> float:

        return (
            self.total
            - self.used
        )

    @property
    def utilization(
        self,
    ) -> float:

        if self.total == 0:
            return 0.0

        return (
            self.used
            / self.total
        )