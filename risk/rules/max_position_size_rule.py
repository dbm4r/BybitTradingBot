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


class MaxPositionSizeRule(BaseRiskRule):

    def __init__(
        self,
        max_quantity: float,
    ):

        self._max_quantity = max_quantity

    @property
    def name(self) -> str:

        return "Max Position Size"

    @property
    def priority(self) -> int:

        return 200

    def evaluate(
        self,
        context: RiskContext,
    ) -> RiskRuleResult:

        quantity = context.position_size.quantity

        if quantity <= self._max_quantity:

            return RiskRuleResult.success()

        return RiskRuleResult.failure(

            RiskViolation(
                rule="MAX_POSITION_SIZE",
                message="Position size exceeds configured maximum.",
                value=quantity,
                limit=self._max_quantity,
            )

        )