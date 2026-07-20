from risk.engine.risk_engine import (
    RiskEngine,
)

from risk.framework.base_risk_rule import (
    BaseRiskRule,
)

from risk.framework.risk_pipeline_builder import (
    RiskPipelineBuilder,
)

from risk.registry.risk_rule_registry import (
    RiskRuleRegistry,
)

from risk.rules.capital_rule import (
    CapitalRule,
)

from risk.rules.max_open_positions_rule import (
    MaxOpenPositionsRule,
)

from risk.rules.max_portfolio_exposure_rule import (
    MaxPortfolioExposureRule,
)

from risk.rules.max_position_size_rule import (
    MaxPositionSizeRule,
)


class RiskEngineBuilder:

    def __init__(
        self,
    ):

        self._pipeline = (
            RiskPipelineBuilder()
        )

    def add_rule(
        self,
        rule: BaseRiskRule,
    ):

        self._pipeline.add(
            rule,
        )

        return self

    def add_rules(
        self,
        *rules: BaseRiskRule,
    ):

        self._pipeline.add_many(
            *rules,
        )

        return self

    def with_registry(
        self,
        registry: RiskRuleRegistry,
    ):

        self._pipeline.add_many(
            *registry.rules,
        )

        return self

    def with_default_rules(
        self,
    ):

        registry = (
            RiskRuleRegistry()
            .register(
                CapitalRule(),
                category="Capital",
            )
            .register(
                MaxPositionSizeRule(
                    max_quantity=100,
                ),
                category="Position",
            )
            .register(
                MaxOpenPositionsRule(
                    maximum=10,
                ),
                category="Portfolio",
            )
            .register(
                MaxPortfolioExposureRule(
                    maximum_exposure=1_000_000,
                ),
                category="Portfolio",
            )
        )

        return self.with_registry(
            registry,
        )

    def build(
        self,
    ) -> RiskEngine:

        return RiskEngine(
            pipeline=self._pipeline.build(),
        )