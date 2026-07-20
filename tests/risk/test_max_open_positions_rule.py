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
from risk.rules.max_open_positions_rule import (
    MaxOpenPositionsRule,
)
from strategies.framework.signal_type import SignalType
from strategies.framework.strategy_decision import (
    StrategyDecision,
)


def create_context(
    open_positions: int,
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
            quantity=1,
            risk_amount=100,
            risk_percent=0.01,
            entry_price=100,
            stop_price=95,
        ),
        portfolio=PortfolioManager(),
        available_capital=10000,
        exposure=ExposureSnapshot(
            total_exposure=0,
            long_exposure=0,
            short_exposure=0,
            open_positions=open_positions,
        ),
        budget=RiskBudget(
            total=1000,
        ),
    )


def test_rule_passes():

    rule = MaxOpenPositionsRule(
        maximum=5,
    )

    result = rule.evaluate(
        create_context(2),
    )

    assert result.passed


def test_rule_fails():

    rule = MaxOpenPositionsRule(
        maximum=5,
    )

    result = rule.evaluate(
        create_context(5),
    )

    assert not result.passed

    assert len(result.violations) == 1

    assert (
        result.violations[0].rule
        == "MAX_OPEN_POSITIONS"
    )


def test_priority():

    assert (
        MaxOpenPositionsRule(
            5,
        ).priority
        == 300
    )


def test_name():

    assert (
        MaxOpenPositionsRule(
            5,
        ).name
        == "Max Open Positions"
    )