class ExecutionCoordinator:

    @staticmethod
    def execute_market_order(
        engine,
        order,
        price,
        timestamp,
        on_fill
    ):

        result = engine.exchange.place_market_order(
            symbol=order.symbol,
            side=order.side,
            quantity=order.quantity,
            price=price
        )

        if not result.success:
            raise RuntimeError(result.error)

        order.exchange_order_id = result.order.order_id

        on_fill()