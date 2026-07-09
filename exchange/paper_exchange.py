from exchange.exchange import Exchange
from uuid import uuid4
from exchange.exchange_result import ExchangeResult
from exchange.exchange_order import ExchangeOrder


class PaperExchange(Exchange):

    def place_market_order(
        self,
        symbol,
        side,
        quantity,
        price = None
    ):

        print(
            f"[PAPER] MARKET {side} "
            f"{quantity:.6f} {symbol}"
        )

        exchange_order = ExchangeOrder(
            order_id=str(uuid4()),
            symbol=symbol,
            side=side,
            quantity=quantity,
            status="FILLED",
            average_price=price
        )

        return ExchangeResult(
            success=True,
            order=exchange_order
        )

    def place_limit_order(
        self,
        symbol,
        side,
        quantity,
        price
    ):

        print(
            f"[PAPER] LIMIT {side} "
            f"{quantity:.6f} {symbol}"
            f" @ {price:.2f}"
        )

    def cancel_order(
        self,
        order_id
    ):

        print(
            f"[PAPER] Cancel {order_id}"
        )

    def get_balance(self):

        return 0

    def get_positions(self):

        return []

    def get_open_orders(self):

        return []