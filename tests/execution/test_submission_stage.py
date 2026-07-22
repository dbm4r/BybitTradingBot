from datetime import UTC, datetime

from execution.framework.stages.submission_stage import (
    SubmissionStage,
)

from execution.models.execution_context import (
    ExecutionContext,
)

from exchange.exchange_order import (
    ExchangeOrder,
)

from exchange.exchange_result import (
    ExchangeResult,
)

from models.candle import (
    Candle,
)

from orders.market_order import (
    MarketOrder,
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

from backtesting.portfolio import (
    Portfolio,
)


class DummyOrderManager:

    def __init__(self):

        self.called = False

    def submit(
        self,
        engine,
        order,
    ):

        self.called = True


class DummyExchange:

    def place_market_order(
        self,
        symbol,
        side,
        quantity,
    ):

        return ExchangeResult(
            success=True,
            order=ExchangeOrder(
                order_id="123",
                symbol=symbol,
                side=side,
                quantity=quantity,
                status="FILLED",
                average_price=100,
            ),
        )


class DummyEngine:

    def __init__(self):

        self.order_manager = (
            DummyOrderManager()
        )

        self.exchange = (
            DummyExchange()
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
        portfolio=Portfolio(
            10000,
        ),
        available_capital=9990,
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


def test_submission_stage():

    engine = DummyEngine()

    context = create_context()

    context.order = MarketOrder(
        symbol="BTCUSDT",
        side="BUY",
        quantity=1,
        timestamp=None,
    )

    context = SubmissionStage().execute(
        engine,
        context,
    )

    assert engine.order_manager.called

    assert context.exchange_result.success

    assert (
        context.exchange_result.order.order_id
        == "123"
    )

    assert (
        context.exchange_result.order.symbol
        == "BTCUSDT"
    )