from risk.framework.base_risk_rule import BaseRiskRule
from risk.framework.risk_pipeline_builder import (
    RiskPipelineBuilder,
)
from risk.framework.risk_rule_result import (
    RiskRuleResult,
)


class DummyRule(BaseRiskRule):

    @property
    def name(self):

        return "Dummy"

    @property
    def priority(self):

        return 1

    def evaluate(
        self,
        context,
    ):

        return RiskRuleResult.success()


def test_builder():

    pipeline = (
        RiskPipelineBuilder()
        .add(
            DummyRule(),
        )
        .build()
    )

    assert pipeline.count == 1


def test_add_many():

    pipeline = (
        RiskPipelineBuilder()
        .add_many(
            DummyRule(),
            DummyRule(),
        )
        .build()
    )

    assert pipeline.count == 2