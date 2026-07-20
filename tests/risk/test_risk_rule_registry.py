from risk.framework.base_risk_rule import (
    BaseRiskRule,
)

from risk.framework.risk_rule_result import (
    RiskRuleResult,
)

from risk.registry.risk_rule_registry import (
    RiskRuleRegistry,
)


class RuleA(BaseRiskRule):

    @property
    def name(self):

        return "Rule A"

    @property
    def priority(self):

        return 200

    def evaluate(
        self,
        context,
    ):

        return RiskRuleResult.success()


class RuleB(BaseRiskRule):

    @property
    def name(self):

        return "Rule B"

    @property
    def priority(self):

        return 100

    def evaluate(
        self,
        context,
    ):

        return RiskRuleResult.success()


class RuleAReplacement(BaseRiskRule):

    @property
    def name(self):

        return "Rule A"

    @property
    def priority(self):

        return 50

    def evaluate(
        self,
        context,
    ):

        return RiskRuleResult.success()


def test_register_rule():

    registry = RiskRuleRegistry()

    registry.register(
        RuleA(),
    )

    assert registry.count == 1

    assert registry.get(
        "Rule A"
    ).name == "Rule A"


def test_priority_order():

    registry = RiskRuleRegistry()

    registry.register(
        RuleA(),
    )

    registry.register(
        RuleB(),
    )

    rules = registry.rules

    assert rules[0].name == "Rule B"

    assert rules[1].name == "Rule A"


def test_replace_duplicate():

    registry = RiskRuleRegistry()

    registry.register(
        RuleA(),
    )

    registry.register(
        RuleAReplacement(),
    )

    assert registry.count == 1

    assert registry.get(
        "Rule A"
    ).priority == 50


def test_metadata():

    registry = RiskRuleRegistry()

    registry.register(
        RuleA(),
        category="Portfolio",
    )

    registration = (
        registry.registrations[0]
    )

    assert (
        registration.metadata.name
        == "Rule A"
    )

    assert (
        registration.metadata.priority
        == 200
    )

    assert (
        registration.metadata.category
        == "Portfolio"
    )


def test_fluent_register():

    registry = (
        RiskRuleRegistry()
        .register(
            RuleA(),
        )
        .register(
            RuleB(),
        )
    )

    assert registry.count == 2