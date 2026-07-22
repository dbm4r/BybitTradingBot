from exchange.exchange_order import (
    ExchangeOrder,
)

from exchange.exchange_result import (
    ExchangeResult,
)

from execution.services.order_submission_service import (
    OrderSubmissionService,
)

from orders.market_order import (
    MarketOrder,
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


def test_submit_market_order():

    engine = DummyEngine()

    order = MarketOrder(
        symbol="BTCUSDT",
        side="BUY",
        quantity=1,
        timestamp=None,
    )

    result = (
        OrderSubmissionService.submit(
            engine=engine,
            order=order,
        )
    )

    assert (
        engine.order_manager.called
    )

    assert result.success

    assert (
        result.order.order_id
        == "123"
    )

    assert (
        result.order.symbol
        == "BTCUSDT"
    )