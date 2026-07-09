class TradeEndpoints:

    def __init__(self, client):

        self.client = client

    def place_market_order(
        self,
        symbol: str,
        side: str,
        quantity: float,
        category: str = "linear"
    ):

        body = {
            "category": category,
            "symbol": symbol,
            "side": side,
            "orderType": "Market",
            "qty": str(quantity)
        }

        return self.client.request(
            method="POST",
            endpoint="/v5/order/create",
            body=body,
            auth=True
        )

    def get_positions(
        self,
        symbol: str | None = None,
        category: str = "linear"
    ):

        params = {
            "category": category
        }

        if symbol is not None:
            params["symbol"] = symbol

        return self.client.request(
            method="GET",
            endpoint="/v5/position/list",
            params=params,
            auth=True
        )
    def close_position(
        self,
        symbol: str,
        category: str = "linear"
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

        body = {
            "category": category,
            "symbol": symbol,
            "side": side,
            "orderType": "Market",
            "qty": size,
            "reduceOnly": True
        }

        return self.client.request(
            method="POST",
            endpoint="/v5/order/create",
            body=body,
            auth=True
        )
    def get_open_orders(
        self,
        symbol: str | None = None,
        category: str = "linear"
    ):

        params = {
            "category": category,
            "openOnly": 0
        }

        if symbol is not None:
            params["symbol"] = symbol

        return self.client.request(
            method="GET",
            endpoint="/v5/order/realtime",
            params=params,
            auth=True
        )
    def cancel_order(
        self,
        symbol: str,
        order_id: str,
        category: str = "linear"
    ):

        body = {
            "category": category,
            "symbol": symbol,
            "orderId": order_id
        }

        return self.client.request(
            method="POST",
            endpoint="/v5/order/cancel",
            body=body,
            auth=True
        )
    def place_limit_order(
        self,
        symbol: str,
        side: str,
        quantity: float,
        price: float,
        category: str = "linear"
    ):

        body = {
            "category": category,
            "symbol": symbol,
            "side": side,
            "orderType": "Limit",
            "qty": str(quantity),
            "price": str(price),
            "timeInForce": "GTC"
        }

        return self.client.request(
            method="POST",
            endpoint="/v5/order/create",
            body=body,
            auth=True
        )
    def get_order(
        self,
        order_id: str,
        category: str = "linear"
    ):

        params = {
            "category": category,
            "orderId": order_id
        }

        return self.client.request(
            method="GET",
            endpoint="/v5/order/realtime",
            params=params,
            auth=True
        )