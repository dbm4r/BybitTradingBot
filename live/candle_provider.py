import pandas as pd


class CandleProvider:

    def __init__(
        self,
        client
    ):

        self.client = client

    def latest_candle(
        self,
        symbol,
        interval="1"
    ):

        response = self.client.market.get_kline(
            symbol=symbol,
            interval=interval,
            limit=1
        )

        candle = response["result"]["list"][0]

        return pd.Series(
            {
                "timestamp": pd.to_datetime(
                    int(candle[0]),
                    unit="ms"
                ),
                "open": float(candle[1]),
                "high": float(candle[2]),
                "low": float(candle[3]),
                "close": float(candle[4]),
                "volume": float(candle[5])
            }
        )