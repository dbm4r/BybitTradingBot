from datetime import UTC, datetime

from models.candle import Candle
from portfolio.portfolio_manager import PortfolioManager

from risk.models.exposure_snapshot import (
    ExposureSnapshot,
)

from risk.models.position_size import (
    PositionSize,
)

from risk.models.risk_budget import (
    RiskBudget,
)

from risk.models.risk_context import (
    RiskContext,
)

from risk.rules.max_portfolio_exposure_rule import (
    MaxPortfolioExposureRule,
)

from strategies.framework.signal_type import (
    SignalType,
)

from strategies.framework.strategy_decision import (
    StrategyDecision,
)


def create_context(
    total_exposure: float,
    quantity: float,
):

    candle = Candle(
        symbol="BTCUSDT",
        interval="1",
        timestamp=datetime.now(UTC),
        open=100,
        high=100,
        low=100,
        close=100,
        volume=1,
        turnover=1,
    )


    decision = StrategyDecision(
        signal=SignalType.OPEN_LONG,
        confidence=1,
        reason="test",
        strategy="Dummy",
        candle=candle,
    )


    return RiskContext(
        decision=decision,

        position_size=PositionSize(
            quantity=quantity,
            risk_amount=100,
            risk_percent=0.01,
            entry_price=100,
            stop_price=95,
        ),

        portfolio=PortfolioManager(),

        available_capital=10000,

        exposure=ExposureSnapshot(
            total_exposure=total_exposure,
            long_exposure=total_exposure,
            short_exposure=0,
            open_positions=1,
        ),

        budget=RiskBudget(
            total=1000,
        ),
    )


def test_rule_passes():

    rule = MaxPortfolioExposureRule(
        maximum_exposure=10000,
    )


    result = rule.evaluate(
        create_context(
            total_exposure=5000,
            quantity=20,
        )
    )


    assert result.passed



def test_rule_fails():

    rule = MaxPortfolioExposureRule(
        maximum_exposure=10000,
    )


    result = rule.evaluate(
        create_context(
            total_exposure=9000,
            quantity=20,
        )
    )


    assert not result.passed

    assert len(
        result.violations
    ) == 1


    violation = result.violations[0]


    assert (
        violation.rule
        ==
        "MAX_PORTFOLIO_EXPOSURE"
    )



def test_priority():

    assert (
        MaxPortfolioExposureRule(
            10000,
        ).priority
        ==
        400
    )



def test_name():

    assert (
        MaxPortfolioExposureRule(
            10000,
        ).name
        ==
        "Max Portfolio Exposure"
    )