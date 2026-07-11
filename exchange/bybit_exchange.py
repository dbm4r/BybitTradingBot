from exchange.exchange import Exchange
from exchange.exchange_result import ExchangeResult
from exchange.exchange_order import ExchangeOrder
from bybit.bybit_client import BybitClient
from exchange.exchange_balance import ExchangeBalance
from exchange.exchange_position import ExchangePosition
from exchange.exchange_trade import ExchangeTrade
from exchange.exchange_snapshot import ExchangeSnapshot


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
    def get_open_orders(
        self,
        symbol=None
    ):

        response = self.client.trade.get_open_orders(
            symbol=symbol
        )

        orders = []

        for item in response["result"]["list"]:

            orders.append(
                ExchangeOrder(
                    order_id=item["orderId"],
                    symbol=item["symbol"],
                    side=item["side"],
                    quantity=float(item["qty"]),
                    status=item["orderStatus"],
                    average_price=(
                        float(item["price"])
                        if item["price"]
                        else None
                    )
                )
            )

        return orders
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
    def get_trade_history(self): 
        response = self.client.trade.get_trade_history() 
        trades = [] 
        for item in response["result"]["list"]: 
            trades.append( 
                ExchangeTrade( 
                    trade_id=item["execId"], 
                    order_id=item["orderId"], 
                    symbol=item["symbol"], 
                    side=item["side"], 
                    quantity=float(item["execQty"]), 
                    price=float(item["execPrice"]), 
                    fee=float(item["execFee"]), 
                    timestamp=item["execTime"] 
                ) 
            ) 
        return trades
    def create_snapshot(self):

        return ExchangeSnapshot(
            balance=self.get_balance(),
            positions=self.get_positions(),
            orders=self.get_open_orders(),
            trades=self.get_trade_history()
        )
        





