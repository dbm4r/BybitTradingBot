from datetime import UTC, datetime

from execution.models.execution_context import (
    ExecutionContext,
)

from models.candle import Candle

from portfolio.portfolio_manager import (
    PortfolioManager,
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


def test_execution_context():

    candle = Candle(
        symbol="BTCUSDT",
        interval="1",
        timestamp=datetime.now(UTC),
        open=100,
        high=105,
        low=95,
        close=101,
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

    context = ExecutionContext(
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
        fee=2,
        slippage=0.5,
    )

    assert context.available_capital == 10000

    assert context.position_size.quantity == 10

    assert context.entry_price == 100

    assert context.take_profit_price == 110