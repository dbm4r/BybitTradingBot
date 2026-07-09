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