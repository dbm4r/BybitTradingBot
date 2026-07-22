from datetime import UTC, datetime

from execution.models.execution_context import (
    ExecutionContext,
)

from execution.services.order_request_factory import (
    OrderRequestFactory,
)

from models.candle import Candle

from backtesting.portfolio import (
    Portfolio,
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

    symbol = "BTCUSDT"


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
        portfolio=Portfolio(10000),
        available_capital=10000,
        position_size=PositionSize(
            quantity=2.5,
            risk_amount=100,
            risk_percent=0.01,
            entry_price=100,
            stop_price=98,
        ),
        entry_price=100,
        stop_price=98,
        take_profit_price=105,
        fee=1,
        slippage=0.1,
    )


def test_create_market_buy():

    order = OrderRequestFactory.create_market_buy(
        engine=DummyEngine(),
        context=create_context(),
    )

    assert order.symbol == "BTCUSDT"

    assert order.side == "BUY"

    assert order.quantity == 2.5


def test_create_market_sell():

    timestamp = datetime.now(UTC)

    order = OrderRequestFactory.create_market_sell(
        engine=DummyEngine(),
        quantity=3,
        timestamp=timestamp,
    )

    assert order.symbol == "BTCUSDT"

    assert order.side == "SELL"

    assert order.quantity == 3

    assert order.timestamp == timestamp