from datetime import UTC, datetime

from execution.models.execution_context import (
    ExecutionContext,
)

from execution.services.risk_execution_service import (
    RiskExecutionService,
)

from models.candle import Candle

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
        high=100,
        low=100,
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
            quantity=10,
            risk_amount=100,
            risk_percent=0.01,
            entry_price=100,
            stop_price=95,
        ),
        entry_price=100,
        stop_price=95,
        take_profit_price=110,
        fee=1,
        slippage=0.1,
    )


def test_risk_execution_service():

    engine = DummyEngine()

    execution_decision = (
        RiskExecutionService.evaluate(
            engine=engine,
            context=create_context(),
        )
    )

    assert execution_decision.approved

    assert execution_decision.risk_decision.approved


def test_rejected_execution():

    engine = DummyEngine()

    context = create_context()

    context.available_capital = 1

    execution_decision = (
        RiskExecutionService.evaluate(
            engine=engine,
            context=context,
        )
    )

    assert not execution_decision.approved

    assert not execution_decision.risk_decision.approved