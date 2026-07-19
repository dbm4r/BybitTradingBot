from bybit.endpoints.base_endpoint import BaseEndpoint


class MarketEndpoints(BaseEndpoint):

    def get_server_time(
        self,
    ):

        return self.get(
            "/v5/market/time",
        )

    def get_tickers(
        self,
        category="linear",
        symbol=None,
    ):

        params = {
            "category": category,
        }

        if symbol is not None:
            params["symbol"] = symbol

        return self.get(
            "/v5/market/tickers",
            params=params,
        )

    def get_instruments(
        self,
        category="linear",
        symbol=None,
    ):

        params = {
            "category": category,
        }

        if symbol is not None:
            params["symbol"] = symbol

        return self.get(
            "/v5/market/instruments-info",
            params=params,
        )

    def get_kline(
        self,
        symbol,
        interval,
        limit=200,
        category="linear",
    ):

        params = {
            "category": category,
            "symbol": symbol,
            "interval": interval,
            "limit": limit,
        }

        return self.get(
            "/v5/market/kline",
            params=params,
        )