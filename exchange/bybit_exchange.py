from exchange.exchange import Exchange
from exchange.exchange_result import ExchangeResult
from exchange.exchange_order import ExchangeOrder
from bybit.bybit_client import BybitClient
from exchange.exchange_balance import ExchangeBalance
from exchange.exchange_position import ExchangePosition


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

        response = self.client.account.get_wallet_balance()

        account = response["result"]["list"][0]

        return ExchangeBalance(
            total_equity=float(account["totalEquity"]),
            wallet_balance=float(account["totalWalletBalance"]),
            available_balance=float(account["totalAvailableBalance"])
        )

    def get_positions(self):

        response = self.client.trade.get_positions()
    

        positions = []

        for item in response["result"]["list"]:

            if float(item["size"]) == 0:
                continue

            positions.append(
                ExchangePosition(
                    symbol=item["symbol"],
                    side=item["side"],
                    quantity=float(item["size"]),
                    average_price=float(item["avgPrice"]),
                    unrealized_pnl=float(item["unrealisedPnl"])
                )
            )

        return positions

    def get_open_orders(self):

        raise NotImplementedError