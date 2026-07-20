from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class RiskViolation:

    rule: str

    message: str

    severity: str = "ERROR"

    value: float | None = None

    limit: float | None = None