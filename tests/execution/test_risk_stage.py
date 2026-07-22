from datetime import UTC
from datetime import datetime

from execution.framework.stages.risk_stage import (
    RiskStage,
)

from execution.models.execution_context import (
    ExecutionContext,
)

from portfolio.portfolio_manager import (
    PortfolioManager,
)

from risk.builders.risk_engine_builder import (
    RiskEngineBuilder,
)

from risk.models.position_size import (
    PositionSize,
)

from strategies.framework.signal_type import (
    SignalType,
)

from strategies.framework.strategy_decision import (
    StrategyDecision,
)

from models.candle import (
    Candle,
)


class DummyEngine:

    def __init__(self):

        self.risk_engine = (
            RiskEngineBuilder()
            .with_default_rules()
            .build()
        )


def create_context():

    candle = Candle(
        symbol="BTCUSDT",
        interval="1",
        timestamp=datetime.now(UTC),
        open=100,
        high=101,
        low=99,
        close=100,
        volume=1,
        turnover=1,
    )

    decision = StrategyDecision(
        signal=SignalType.OPEN_LONG,
        confidence=1,
        strategy="Dummy",
        reason="Test",
        candle=candle,
    )

    return ExecutionContext(
        decision=decision,
        portfolio=PortfolioManager(),
        available_capital=10000,
        position_size=PositionSize(
            quantity=1,
            risk_amount=100,
            risk_percent=0.01,
            entry_price=100,
            stop_price=98,
        ),
        entry_price=100,
        stop_price=98,
        take_profit_price=105,
        fee=10,
        slippage=0.001,
    )


def test_risk_stage():

    context = (
        RiskStage().execute(
            DummyEngine(),
            create_context(),
        )
    )

    assert context.risk_decision is not None

    assert context.risk_decision.approved