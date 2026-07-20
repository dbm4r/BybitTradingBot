from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class RiskRuleMetadata:

    name: str

    priority: int

    category: str