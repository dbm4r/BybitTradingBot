from risk.framework.base_risk_rule import (
    BaseRiskRule,
)
from risk.framework.risk_rule_result import (
    RiskRuleResult,
)
from risk.models.risk_context import (
    RiskContext,
)
from risk.models.risk_violation import (
    RiskViolation,
)


class CapitalRule(BaseRiskRule):

    @property
    def name(self) -> str:

        return "Capital Rule"

    @property
    def priority(self) -> int:

        return 100

    def evaluate(
        self,
        context: RiskContext,
    ) -> RiskRuleResult:

        required_capital = (
            context.position_size.quantity
            * context.position_size.entry_price
        )

        if required_capital <= context.available_capital:

            return RiskRuleResult.success()

        return RiskRuleResult.failure(

            RiskViolation(
                rule="CAPITAL",
                message="Insufficient available capital.",
                value=required_capital,
                limit=context.available_capital,
            )

        )