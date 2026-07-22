from datetime import UTC, datetime

from backtesting.portfolio import (
    Portfolio,
)

from exchange.instrument import (
    Instrument,
)

from execution.models.execution_context import (
    ExecutionContext,
)

from execution.services.order_validation_service import (
    OrderValidationService,
)

from models.candle import (
    Candle,
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


class DummyExchange:

    def get_instrument(
        self,
        symbol,
    ):

        return Instrument(
            symbol=symbol,
            qty_step=0.001,
            min_qty=0.001,
            max_qty=100,
            tick_size=0.10,
        )


class DummyEngine:

    symbol = "BTCUSDT"

    exchange = DummyExchange()


def create_context(
    quantity=1.23456,
    available_capital=10000,
):

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
        available_capital=available_capital,
        position_size=PositionSize(
            quantity=quantity,
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


def test_validate_rounds_quantity():

    position_size = (
        OrderValidationService.validate(
            engine=DummyEngine(),
            context=create_context(),
        )
    )

    assert (
        position_size.quantity
        == 1.234
    )


def test_validate_rejects_invalid_quantity():

    context = create_context(
        quantity=1000,
        available_capital=1_000_000,
    )

    try:

        OrderValidationService.validate(
            engine=DummyEngine(),
            context=context,
        )

        assert False

    except RuntimeError:

        assert True