from exchange.exchange import Exchange
from exchange.exchange_result import ExchangeResult
from exchange.exchange_order import ExchangeOrder
from bybit.bybit_client import BybitClient


class BybitExchange(Exchange):

    def __init__(
        self,
        api_key,
        api_secret,
        base_url
    ):

        self.client = BybitClient(
            api_key=api_key,
            api_secret=api_secret,
            base_url=base_url
        )

    def place_market_order(
        self,
        symbol,
        side,
        quantity,
        price=None
    ):

        response = self.client.trade.place_market_order(
            symbol=symbol,
            side=side,
            quantity=quantity
        )

        if response["retCode"] != 0:

            return ExchangeResult(
                success=False,
                order=None,
                error=response["retMsg"]
            )

        exchange_order = ExchangeOrder(
            order_id=response["result"]["orderId"],
            symbol=symbol,
            side=side,
            quantity=quantity,
            status="NEW",
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

        response = self.client.trade.place_limit_order(
            symbol=symbol,
            side=side,
            quantity=quantity,
            price=price
        )

        if response["retCode"] != 0:

            return ExchangeResult(
                success=False,
                order=None,
                error=response["retMsg"]
            )

        exchange_order = ExchangeOrder(
            order_id=response["result"]["orderId"],
            symbol=symbol,
            side=side,
            quantity=quantity,
            status="NEW",
            average_price=None
        )

        return ExchangeResult(
            success=True,
            order=exchange_order
        )

    def cancel_order(
        self,
        symbol,
        order_id
    ):

        return self.client.trade.cancel_order(
            symbol=symbol,
            order_id=order_id
        )

    def get_balance(self):

        return self.client.account.get_wallet_balance()

    def get_positions(
        self,
        symbol=None
    ):

        return self.client.trade.get_positions(
            symbol=symbol
        )

    def get_open_orders(
        self,
        symbol=None
    ):

        return self.client.trade.get_open_orders(
            symbol=symbol
        )
    def get_order(
        self,
        order_id
    ):

        return self.client.trade.get_order(
            order_id=order_id
        )
    def amend_order(
        self,
        symbol,
        order_id,
        price=None,
        quantity=None
    ):

        return self.client.trade.amend_order(
            symbol=symbol,
            order_id=order_id,
            price=price,
            quantity=quantity
        )