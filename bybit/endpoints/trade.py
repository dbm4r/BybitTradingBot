class TradeEndpoints:

    DEFAULT_CATEGORY = "linear"
    DEFAULT_SETTLE_COIN = "USDT"

    def __init__(self, client):

        self.client = client

    def _build_linear_params(
        self,
        symbol=None,
        settle_coin=DEFAULT_SETTLE_COIN,
        category=DEFAULT_CATEGORY
    ):

        params = {
            "category": category
        }

        if symbol is not None:
            params["symbol"] = symbol
        else:
            params["settleCoin"] = settle_coin

        return params

    def _build_linear_body(
        self,
        symbol,
        category=DEFAULT_CATEGORY
    ):

        return {
            "category": category,
            "symbol": symbol
        }

    def place_market_order(
        self,
        symbol: str,
        side: str,
        quantity: float,
        category: str = DEFAULT_CATEGORY
    ):

        body = self._build_linear_body(
            symbol=symbol,
            category=category
        )

        body.update({
            "side": side,
            "orderType": "Market",
            "qty": str(quantity)
        })

        return self.client.request(
            method="POST",
            endpoint="/v5/order/create",
            body=body,
            auth=True
        )

    def place_limit_order(
        self,
        symbol: str,
        side: str,
        quantity: float,
        price: float,
        category: str = DEFAULT_CATEGORY
    ):

        body = self._build_linear_body(
            symbol=symbol,
            category=category
        )

        body.update({
            "side": side,
            "orderType": "Limit",
            "qty": str(quantity),
            "price": str(price),
            "timeInForce": "GTC"
        })

        return self.client.request(
            method="POST",
            endpoint="/v5/order/create",
            body=body,
            auth=True
        )

    def get_positions(
        self,
        symbol: str | None = None,
        settle_coin: str = DEFAULT_SETTLE_COIN,
        category: str = DEFAULT_CATEGORY
    ):

        params = self._build_linear_params(
            symbol=symbol,
            settle_coin=settle_coin,
            category=category
        )

        return self.client.request(
            method="GET",
            endpoint="/v5/position/list",
            params=params,
            auth=True
        )

    def get_open_orders(
        self,
        symbol: str | None = None,
        settle_coin: str = DEFAULT_SETTLE_COIN,
        category: str = DEFAULT_CATEGORY
    ):

        params = self._build_linear_params(
            symbol=symbol,
            settle_coin=settle_coin,
            category=category
        )

        params["openOnly"] = 0

        return self.client.request(
            method="GET",
            endpoint="/v5/order/realtime",
            params=params,
            auth=True
        )

    def get_order(
        self,
        order_id: str,
        settle_coin: str = DEFAULT_SETTLE_COIN,
        category: str = DEFAULT_CATEGORY
    ):

        params = self._build_linear_params(
            settle_coin=settle_coin,
            category=category
        )

        params["orderId"] = order_id

        return self.client.request(
            method="GET",
            endpoint="/v5/order/realtime",
            params=params,
            auth=True
        )

    def amend_order(
        self,
        symbol: str,
        order_id: str,
        price: float | None = None,
        quantity: float | None = None,
        category: str = DEFAULT_CATEGORY
    ):

        body = self._build_linear_body(
            symbol=symbol,
            category=category
        )

        body["orderId"] = order_id

        if price is not None:
            body["price"] = str(price)

        if quantity is not None:
            body["qty"] = str(quantity)

        return self.client.request(
            method="POST",
            endpoint="/v5/order/amend",
            body=body,
            auth=True
        )

    def cancel_order(
        self,
        symbol: str,
        order_id: str,
        category: str = DEFAULT_CATEGORY
    ):

        body = self._build_linear_body(
            symbol=symbol,
            category=category
        )

        body["orderId"] = order_id

        return self.client.request(
            method="POST",
            endpoint="/v5/order/cancel",
            body=body,
            auth=True
        )

    def close_position(
        self,
        symbol: str,
        category: str = DEFAULT_CATEGORY
    ):

        positions = self.get_positions(
            symbol=symbol,
            category=category
        )

        position = positions["result"]["list"][0]

        size = position["size"]

        if float(size) == 0:
            return {
                "message": "No open position."
            }

        side = (
            "Sell"
            if position["side"] == "Buy"
            else "Buy"
        )

        body = self._build_linear_body(
            symbol=symbol,
            category=category
        )

        body.update({
            "side": side,
            "orderType": "Market",
            "qty": size,
            "reduceOnly": True
        })

        return self.client.request(
            method="POST",
            endpoint="/v5/order/create",
            body=body,
            auth=True
        )

    def get_trade_history(
        self,
        symbol: str | None = None,
        settle_coin: str = DEFAULT_SETTLE_COIN,
        category: str = DEFAULT_CATEGORY,
        limit: int = 50
    ):

        params = self._build_linear_params(
            symbol=symbol,
            settle_coin=settle_coin,
            category=category
        )

        params["limit"] = limit

        return self.client.request(
            method="GET",
            endpoint="/v5/execution/list",
            params=params,
            auth=True
        )