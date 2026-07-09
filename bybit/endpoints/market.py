class MarketEndpoints:

    def __init__(self, client):

        self.client = client
    def get_server_time(self):

        return self.client.request(
            method="GET",
            endpoint="/v5/market/time"
        )
    def get_tickers(
        self,
        category="linear",
        symbol=None
    ):

        params = {
            "category": category
        }

        if symbol is not None:
            params["symbol"] = symbol

        return self.client.request(
            method="GET",
            endpoint="/v5/market/tickers",
            params=params
        )
    def get_instruments(
        self,
        category="linear",
        symbol=None
    ):

        params = {
            "category": category
        }

        if symbol is not None:
            params["symbol"] = symbol

        return self.client.request(
            method="GET",
            endpoint="/v5/market/instruments-info",
            params=params
        )
    def get_kline(
        self,
        symbol,
        interval,
        limit=200,
        category="linear"
    ):

        params = {
            "category": category,
            "symbol": symbol,
            "interval": interval,
            "limit": limit
        }

        return self.client.request(
            method="GET",
            endpoint="/v5/market/kline",
            params=params
        )