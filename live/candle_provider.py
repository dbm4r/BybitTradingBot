import pandas as pd


class CandleProvider:

    def __init__(
        self,
        client
    ):

        self.client = client
        self.dataframe = None
        self.last_timestamp = None

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
        timestamp = candle["timestamp"]

        if timestamp == self.last_timestamp:
            return None

        self.last_timestamp = timestamp

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
    def append_candle(
        self,
        candle
    ):

        row = pd.DataFrame(
            [
                {
                    "timestamp": pd.to_datetime(
                        candle["start"],
                        unit="ms",
                        utc=True
                    ),
                    "open": float(candle["open"]),
                    "high": float(candle["high"]),
                    "low": float(candle["low"]),
                    "close": float(candle["close"]),
                    "volume": float(candle["volume"])
                }
            ]
        )

        timestamp = row.iloc[0]["timestamp"]

        if timestamp == self.last_timestamp:
            return None

        self.last_timestamp = timestamp

        self.dataframe = pd.concat(
            [
                self.dataframe,
                row
            ],
            ignore_index=True
        )

        self.dataframe = (
            self.dataframe
            .tail(200)
            .reset_index(drop=True)
        )

        return self.dataframe