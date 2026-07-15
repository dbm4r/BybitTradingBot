from models.candle import Candle


class CandleAggregator:

    @staticmethod
    def aggregate(
        candles: list[Candle],
        interval: str,
    ) -> Candle:

        if not candles:
            raise ValueError(
                "Cannot aggregate an empty candle list."
            )

        first = candles[0]

        last = candles[-1]

        data = {
            "timestamp": first.timestamp,
            "open": first.open,
            "high": max(
                candle.high
                for candle in candles
            ),
            "low": min(
                candle.low
                for candle in candles
            ),
            "close": last.close,
            "volume": sum(
                candle.volume
                for candle in candles
            ),
            "turnover": sum(
                candle.turnover
                for candle in candles
            ),
        }

        return Candle.from_dict(
            symbol=first.symbol,
            interval=interval,
            data=data,
        )