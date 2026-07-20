from risk.builders.risk_engine_builder import (
    RiskEngineBuilder,
)

from risk.engine.risk_engine import (
    RiskEngine,
)

from risk.framework.base_risk_rule import (
    BaseRiskRule,
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

    engine = (
        RiskEngineBuilder()
        .add_rule(
            DummyRule()
        )
        .build()
    )

    assert isinstance(
        engine,
        RiskEngine,
    )

    assert (
        engine.pipeline.count
        == 1
    )


def test_multiple_rules():

    engine = (
        RiskEngineBuilder()
        .add_rules(
            DummyRule(),
            DummyRule(),
        )
        .build()
    )

    assert (
        engine.pipeline.count
        == 2
    )