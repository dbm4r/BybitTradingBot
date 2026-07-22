from execution.models.execution_context import (
    ExecutionContext,
)

from orders.market_order import (
    MarketOrder,
)


class ExitOrderRequestFactory:

    @staticmethod
    def create(
        engine,
        context: ExecutionContext,
        timestamp,
    ) -> MarketOrder:

        return MarketOrder(
            symbol=engine.symbol,
            side="SELL",
            quantity=context.position_size.quantity,
            timestamp=timestamp,
        )