from exchange.exchange_result import (
    ExchangeResult,
)

from orders.order import (
    Order,
)


class OrderSubmissionService:

    @staticmethod
    def submit(
        engine,
        order: Order,
    ) -> ExchangeResult:

        engine.order_manager.submit(
            engine,
            order,
        )

        result = (
            engine.exchange.place_market_order(
                symbol=order.symbol,
                side=order.side,
                quantity=order.quantity,
            )
        )

        print("\n========== EXCHANGE RESULT ==========")
        print("Success :", result.success)
        print(
            "Order ID:",
            result.order.order_id
            if result.order
            else None,
        )
        print("=====================================\n")

        if not result.success:

            raise RuntimeError(
                result.error,
            )

        return result