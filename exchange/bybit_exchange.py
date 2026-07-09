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
                order=None
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

        raise NotImplementedError

    def cancel_order(
        self,
        order_id
    ):

        raise NotImplementedError

    def get_balance(self):

        return self.client.account.get_wallet_balance()

    def get_positions(self):

        return self.client.trade.get_positions()

    def get_open_orders(self):

        raise NotImplementedError