from datetime import UTC
from datetime import datetime

import pytest

from backtesting.portfolio import (
    Portfolio,
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

from risk.builders.risk_engine_builder import (
    RiskEngineBuilder,
)

from risk.models.position_size import (
    PositionSize,
)

from risk.sizing.fixed_risk_sizer import (
    FixedRiskSizer,
)

from strategies.framework.signal_type import (
    SignalType,
)

from strategies.framework.strategy_decision import (
    StrategyDecision,
)


class DummySettings:

    trading_fee = 0.001

    slippage_percent = 0.001

    stop_loss_percent = 0.02

    take_profit_percent = 0.05

    risk_per_trade = 0.01


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

        self.settings = DummySettings()

        self.portfolio = Portfolio(
            10000,
        )

        self.position_sizer = (
            FixedRiskSizer()
        )

        self.risk_engine = (
            RiskEngineBuilder()
            .with_default_rules()
            .build()
        )

        self.order_manager = (
            DummyOrderManager()
        )

        self.exchange = (
            DummyExchange()
        )


@pytest.fixture
def engine():

    return DummyEngine()


@pytest.fixture
def candle():

    return Candle(
        symbol="BTCUSDT",
        interval="1",
        timestamp=datetime.now(
            UTC,
        ),
        open=100,
        high=101,
        low=99,
        close=100,
        volume=1,
        turnover=1,
    )


@pytest.fixture
def decision(
    candle,
):

    return StrategyDecision(
        signal=SignalType.OPEN_LONG,
        confidence=1,
        strategy="Dummy",
        reason="Test",
        candle=candle,
    )


@pytest.fixture
def context(
    decision,
):

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


@pytest.fixture
def order():

    return MarketOrder(
        symbol="BTCUSDT",
        side="BUY",
        quantity=1,
        timestamp=None,
    )