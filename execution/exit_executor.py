from orders.market_order import MarketOrder
from finance.slippage_calculator import SlippageCalculator
from execution.fill_processor import FillProcessor
class ExitExecutor:

    @staticmethod
    def execute(
        engine,
        timestamp,
        price,
        exit_reason
    ):
        position = engine.portfolio.get_position(
            engine.symbol
        )
        price = SlippageCalculator.apply_sell(
            price=price,
            slippage_percent=engine.settings.slippage_percent
        )

        order = MarketOrder(
            symbol=engine.symbol,
            side="SELL",
            quantity=position.quantity,
            timestamp=timestamp
        )

        engine.order_manager.submit(
            engine,
            order
        )
        result = engine.exchange.place_market_order(
            symbol=order.symbol,
            side=order.side,
            quantity=order.quantity
        )

        if not result.success:
            raise RuntimeError(result.error)

        exchange_order = result.order

        order.exchange_order_id = exchange_order.order_id

        FillProcessor.process_exit_fill(
            engine=engine,
            order=order,
            timestamp=timestamp,
            price=price,
            exit_reason=exit_reason
        )