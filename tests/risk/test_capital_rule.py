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
from risk.rules.capital_rule import (
    CapitalRule,
)
from strategies.framework.signal_type import SignalType
from strategies.framework.strategy_decision import (
    StrategyDecision,
)


def create_context(
    capital: float,
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
        available_capital=capital,
        exposure=ExposureSnapshot(
            total_exposure=0,
            long_exposure=0,
            short_exposure=0,
            open_positions=0,
        ),
        budget=RiskBudget(
            total=1000,
        ),
    )


def test_capital_pass():

    rule = CapitalRule()

    result = rule.evaluate(
        create_context(
            capital=10000,
            quantity=10,
        )
    )

    assert result.passed


def test_capital_fail():

    rule = CapitalRule()

    result = rule.evaluate(
        create_context(
            capital=100,
            quantity=10,
        )
    )

    assert not result.passed

    assert len(result.violations) == 1


def test_priority():

    assert CapitalRule().priority == 100


def test_name():

    assert CapitalRule().name == "Capital Rule"