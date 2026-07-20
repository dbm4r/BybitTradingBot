import pandas as pd


class CandleDataFrameMapper:

    @staticmethod
    def map(
        candles,
    ) -> pd.DataFrame:

        dataframe = pd.DataFrame(
            [
                {
                    "timestamp": candle.timestamp,
                    "open": candle.open,
                    "high": candle.high,
                    "low": candle.low,
                    "close": candle.close,
                    "volume": candle.volume,
                }
                for candle in candles
            ]
        )

        dataframe["timestamp"] = pd.to_datetime(
            dataframe["timestamp"],
            utc=True,
        )

        return dataframe