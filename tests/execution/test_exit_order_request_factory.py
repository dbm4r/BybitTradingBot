from datetime import UTC, datetime

from backtesting.portfolio import (
    Portfolio,
)

from execution.models.execution_context import (
    ExecutionContext,
)

from execution.services.exit_order_request_factory import (
    ExitOrderRequestFactory,
)

from risk.models.position_size import (
    PositionSize,
)


def test_create_exit_market_order():

    timestamp = datetime.now(UTC)

    context = ExecutionContext(
        decision=None,
        portfolio=Portfolio(10000),
        available_capital=10000,
        position_size=PositionSize(
            quantity=2.5,
            risk_amount=0,
            risk_percent=0,
            entry_price=100,
            stop_price=100,
        ),
        entry_price=100,
        stop_price=100,
        take_profit_price=100,
        fee=0,
        slippage=0,
    )

    order = ExitOrderRequestFactory.create(
        engine=type(
            "DummyEngine",
            (),
            {
                "symbol": "BTCUSDT",
            },
        )(),
        context=context,
        timestamp=timestamp,
    )

    assert order.symbol == "BTCUSDT"

    assert order.side == "SELL"

    assert order.quantity == 2.5

    assert order.timestamp == timestamp