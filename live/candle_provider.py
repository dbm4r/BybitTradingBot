import pandas as pd


class CandleProvider:

    def __init__(
        self,
        client
    ):

        self.client = client
        self.dataframe = None

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
    def initialize(
        self,
        symbol,
        interval="1",
        limit=200
    ):

        response = self.client.market.get_kline(
            symbol=symbol,
            interval=interval,
            limit=limit
        )

        candles = response["result"]["list"]

        rows = []

        for candle in reversed(candles):

            rows.append({
                "timestamp": pd.to_datetime(
                    int(candle[0]),
                    unit="ms",
                    utc=True
                ),
                "open": float(candle[1]),
                "high": float(candle[2]),
                "low": float(candle[3]),
                "close": float(candle[4]),
                "volume": float(candle[5])
            })

        self.dataframe = pd.DataFrame(rows)

        return self.dataframe
    def update(
        self,
        symbol,
        interval="1"
    ):

        candle = self.latest_candle(
            symbol=symbol,
            interval=interval
        )

        self.dataframe = pd.concat(
            [
                self.dataframe,
                candle.to_frame().T
            ],
            ignore_index=True
        )

        self.dataframe = (
            self.dataframe
            .tail(200)
            .reset_index(drop=True)
        )

        return self.dataframe