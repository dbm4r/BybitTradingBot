from risk.framework.base_risk_rule import (
    BaseRiskRule,
)
from risk.framework.risk_rule_result import (
    RiskRuleResult,
)
from risk.models.risk_context import (
    RiskContext,
)


class RiskPipeline:

    def __init__(self):

        self._rules: list[
            BaseRiskRule
        ] = []

    def add(
        self,
        rule: BaseRiskRule,
    ):

        self._rules.append(
            rule,
        )

        self._rules.sort(
            key=lambda rule: rule.priority
        )

    def add_many(
        self,
        *rules: BaseRiskRule,
    ):

        for rule in rules:

            self.add(
                rule,
            )

    @property
    def rules(
        self,
    ):

        return tuple(
            self._rules
        )

    @property
    def count(
        self,
    ):

        return len(
            self._rules
        )

    def evaluate(
        self,
        context: RiskContext,
    ):

        return tuple(

            rule.evaluate(
                context,
            )

            for rule in self._rules
        )