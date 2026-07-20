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


class MaxOpenPositionsRule(
    BaseRiskRule,
):

    def __init__(
        self,
        maximum: int,
    ):

        self._maximum = maximum

    @property
    def name(
        self,
    ) -> str:

        return "Max Open Positions"

    @property
    def priority(
        self,
    ) -> int:

        return 300

    def evaluate(
        self,
        context: RiskContext,
    ) -> RiskRuleResult:

        positions = (
            context.exposure.open_positions
        )

        if positions < self._maximum:

            return RiskRuleResult.success()

        return RiskRuleResult.failure(

            RiskViolation(
                rule="MAX_OPEN_POSITIONS",
                message="Maximum number of open positions reached.",
                value=positions,
                limit=self._maximum,
            )

        )