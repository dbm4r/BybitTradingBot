from risk.builders.risk_engine_builder import (
    RiskEngineBuilder,
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


def test_builder_with_registry():

    registry = (
        RiskRuleRegistry()
        .register(
            CapitalRule(),
        )
        .register(
            MaxPositionSizeRule(
                max_quantity=10,
            ),
        )
    )

    engine = (
        RiskEngineBuilder()
        .with_registry(
            registry,
        )
        .build()
    )

    assert engine.pipeline.count == 2


def test_builder_with_default_rules():

    engine = (
        RiskEngineBuilder()
        .with_default_rules()
        .build()
    )

    assert engine.pipeline.count == 4


def test_default_rule_order():

    engine = (
        RiskEngineBuilder()
        .with_default_rules()
        .build()
    )

    names = tuple(

        rule.name

        for rule

        in engine.pipeline.rules

    )

    assert names == (
        "Capital Rule",
        "Max Position Size",
        "Max Open Positions",
        "Max Portfolio Exposure",
    )


def test_registry_rules_are_sorted():

    registry = (
        RiskRuleRegistry()
        .register(
            MaxPortfolioExposureRule(
                maximum_exposure=1000,
            ),
        )
        .register(
            CapitalRule(),
        )
        .register(
            MaxOpenPositionsRule(
                maximum=5,
            ),
        )
        .register(
            MaxPositionSizeRule(
                max_quantity=10,
            ),
        )
    )

    engine = (
        RiskEngineBuilder()
        .with_registry(
            registry,
        )
        .build()
    )

    priorities = tuple(

        rule.priority

        for rule

        in engine.pipeline.rules

    )

    assert priorities == (
        100,
        200,
        300,
        400,
    )