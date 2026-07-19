import pandas as pd

from models.candle import Candle


class DataDownloader:

    @staticmethod
    def save_to_csv(
        df: pd.DataFrame,
        filename: str,
    ) -> None:

        df.to_csv(
            filename,
            index=False,
        )

    @staticmethod
    def from_candles(
        candles: list[Candle],
    ) -> pd.DataFrame:

        rows = []

        for candle in candles:

            rows.append(
                {
                    "timestamp": candle.timestamp,
                    "open": candle.open,
                    "high": candle.high,
                    "low": candle.low,
                    "close": candle.close,
                    "volume": candle.volume,
                    "turnover": candle.turnover,
                }
            )

        df = pd.DataFrame(rows)

        if df.empty:
            return df

        df = (
            df.sort_values("timestamp")
              .reset_index(drop=True)
        )

        return df