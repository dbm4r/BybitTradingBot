from dataclasses import dataclass

from risk.framework.base_risk_rule import (
    BaseRiskRule,
)

from risk.registry.risk_rule_metadata import (
    RiskRuleMetadata,
)


@dataclass(
    frozen=True,
    slots=True,
)
class RiskRuleRegistration:

    metadata: RiskRuleMetadata

    rule: BaseRiskRule