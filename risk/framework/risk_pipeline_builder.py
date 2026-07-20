from risk.framework.base_risk_rule import (
    BaseRiskRule,
)
from risk.framework.risk_pipeline import (
    RiskPipeline,
)


class RiskPipelineBuilder:

    def __init__(
        self,
    ):

        self._pipeline = (
            RiskPipeline()
        )

    def add(
        self,
        rule: BaseRiskRule,
    ):

        self._pipeline.add(
            rule,
        )

        return self

    def add_many(
        self,
        *rules: BaseRiskRule,
    ):

        self._pipeline.add_many(
            *rules,
        )

        return self

    def build(
        self,
    ) -> RiskPipeline:

        return self._pipeline