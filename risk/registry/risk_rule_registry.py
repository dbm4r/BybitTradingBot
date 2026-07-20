from risk.framework.base_risk_rule import (
    BaseRiskRule,
)

from risk.registry.risk_rule_metadata import (
    RiskRuleMetadata,
)

from risk.registry.risk_rule_registration import (
    RiskRuleRegistration,
)


class RiskRuleRegistry:

    def __init__(
        self,
    ):

        self._rules: dict[
            str,
            RiskRuleRegistration,
        ] = {}

    def register(
        self,
        rule: BaseRiskRule,
        category: str = "General",
    ):

        metadata = RiskRuleMetadata(
            name=rule.name,
            priority=rule.priority,
            category=category,
        )

        registration = (
            RiskRuleRegistration(
                metadata=metadata,
                rule=rule,
            )
        )

        self._rules[
            rule.name
        ] = registration

        return self

    def get(
        self,
        name: str,
    ) -> BaseRiskRule:

        return self._rules[
            name
        ].rule

    @property
    def registrations(
        self,
    ) -> tuple[
        RiskRuleRegistration,
        ...
    ]:

        return tuple(
            sorted(
                self._rules.values(),
                key=lambda registration:
                registration.metadata.priority,
            )
        )

    @property
    def rules(
        self,
    ) -> tuple[
        BaseRiskRule,
        ...
    ]:

        return tuple(

            registration.rule

            for registration

            in self.registrations

        )

    @property
    def count(
        self,
    ) -> int:

        return len(
            self._rules
        )