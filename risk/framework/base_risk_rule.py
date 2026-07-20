from abc import ABC
from abc import abstractmethod

from risk.framework.risk_rule_result import (
    RiskRuleResult,
)
from risk.models.risk_context import (
    RiskContext,
)


class BaseRiskRule(
    ABC,
):

    @property
    @abstractmethod
    def name(
        self,
    ) -> str:
        ...

    @property
    @abstractmethod
    def priority(
        self,
    ) -> int:
        ...

    @abstractmethod
    def evaluate(
        self,
        context: RiskContext,
    ) -> RiskRuleResult:
        ...