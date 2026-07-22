from execution.models.execution_context import (
    ExecutionContext,
)

from orders.market_order import (
    MarketOrder,
)


class OrderRequestFactory:

    @staticmethod
    def create_market_buy(
        engine,
        context: ExecutionContext,
    ) -> MarketOrder:

        return MarketOrder(
            symbol=engine.symbol,
            side="BUY",
            quantity=context.position_size.quantity,
            timestamp=context.decision.candle.timestamp,
        )

    @staticmethod
    def create_market_sell(
        engine,
        quantity: float,
        timestamp,
    ) -> MarketOrder:

        return MarketOrder(
            symbol=engine.symbol,
            side="SELL",
            quantity=quantity,
            timestamp=timestamp,
        )