
from datetime import datetime, timezone
from market.candle_factory import CandleFactory
from models.candle_series import CandleSeries

class CandleProvider:

    def __init__(self, client):

        self.client = client
        self.last_timestamp = None

    def latest_candle(
        self,
        symbol,
        interval="1",
    ):

        response = self.client.market.get_kline(
            symbol=symbol,
            interval=interval,
            limit=1,
        )

        candle = response["result"]["list"][0]

        return CandleFactory.from_dict(
            symbol=symbol,
            interval=interval,
            data={
                "timestamp": datetime.fromtimestamp(
                    int(candle[0]) / 1000,
                    tz=timezone.utc,
                ),
                "open": candle[1],
                "high": candle[2],
                "low": candle[3],
                "close": candle[4],
                "volume": candle[5],
                "turnover": 0,
            },
        )

    def initialize(
        self,
        symbol,
        interval="1",
        limit=200,
    ):

        response = self.client.market.get_kline(
            symbol=symbol,
            interval=interval,
            limit=limit,
        )

        candles = []

        for item in reversed(response["result"]["list"]):

            candles.append(
                CandleFactory.from_dict(
                    symbol=symbol,
                    interval=interval,
                    data={
                        "timestamp": datetime.fromtimestamp(
                            int(item[0]) / 1000,
                            tz=timezone.utc,
                        ),
                        "open": item[1],
                        "high": item[2],
                        "low": item[3],
                        "close": item[4],
                        "volume": item[5],
                        "turnover": 0,
                    },
                )
            )

        return CandleSeries(
            symbol=symbol,
            interval=interval,
            candles=candles,
        )

    def update(
        self,
        symbol,
        interval="1",
    ):

        candle = self.latest_candle(
            symbol=symbol,
            interval=interval,
        )

        if candle.timestamp == self.last_timestamp:
            return None

        self.last_timestamp = candle.timestamp

        return candle