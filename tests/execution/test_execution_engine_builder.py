from backtesting.portfolio import (
    Portfolio,
)

from core.settings import (
    Settings,
)

from execution.builders.execution_engine_builder import (
    ExecutionEngineBuilder,
)

from risk.builders.risk_engine_builder import (
    RiskEngineBuilder,
)

from risk.sizing.fixed_risk_sizer import (
    FixedRiskSizer,
)


class DummyStrategy:

    name = "Dummy"

    parameters = {}


def test_build_execution_engine():

    engine = (
        ExecutionEngineBuilder()
        .with_portfolio(
            Portfolio(10000),
        )
        .with_settings(
            Settings(),
        )
        .with_symbol(
            "BTCUSDT",
        )
        .with_strategy(
            DummyStrategy(),
        )
        .with_exchange(
            "PAPER",
        )
        .build()
    )

    assert engine.symbol == "BTCUSDT"

    assert engine.strategy.name == "Dummy"

    assert engine.portfolio.cash == 10000


def test_custom_position_sizer():

    sizer = FixedRiskSizer()

    engine = (
        ExecutionEngineBuilder()
        .with_portfolio(
            Portfolio(10000),
        )
        .with_settings(
            Settings(),
        )
        .with_symbol(
            "BTCUSDT",
        )
        .with_strategy(
            DummyStrategy(),
        )
        .with_exchange(
            "PAPER",
        )
        .with_position_sizer(
            sizer,
        )
        .build()
    )

    assert (
        engine.position_sizer
        is sizer
    )


def test_custom_risk_engine():

    risk_engine = (
        RiskEngineBuilder()
        .with_default_rules()
        .build()
    )

    engine = (
        ExecutionEngineBuilder()
        .with_portfolio(
            Portfolio(10000),
        )
        .with_settings(
            Settings(),
        )
        .with_symbol(
            "BTCUSDT",
        )
        .with_strategy(
            DummyStrategy(),
        )
        .with_exchange(
            "PAPER",
        )
        .with_risk_engine(
            risk_engine,
        )
        .build()
    )

    assert (
        engine.risk_engine
        is risk_engine
    )