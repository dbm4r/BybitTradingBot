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


class MaxPortfolioExposureRule(
    BaseRiskRule,
):

    def __init__(
        self,
        maximum_exposure: float,
    ):

        self._maximum_exposure = maximum_exposure


    @property
    def name(
        self,
    ) -> str:

        return "Max Portfolio Exposure"


    @property
    def priority(
        self,
    ) -> int:

        return 400


    def evaluate(
        self,
        context: RiskContext,
    ) -> RiskRuleResult:

        current_exposure = (
            context.exposure.total_exposure
        )

        new_exposure = (
            current_exposure
            +
            context.position_size.notional
        )


        if new_exposure <= self._maximum_exposure:

            return RiskRuleResult.success()


        return RiskRuleResult.failure(

            RiskViolation(
                rule="MAX_PORTFOLIO_EXPOSURE",
                message="Portfolio exposure limit exceeded.",
                value=new_exposure,
                limit=self._maximum_exposure,
            )

        )