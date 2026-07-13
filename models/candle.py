from dataclasses import dataclass
from datetime import datetime

import pandas as pd


@dataclass(slots=True, frozen=True)
class Candle:

    symbol: str
    interval: str
    timestamp: datetime

    open: float
    high: float
    low: float
    close: float

    volume: float
    turnover: float

    @property
    def is_bullish(self) -> bool:
        return self.close > self.open

    @property
    def is_bearish(self) -> bool:
        return self.close < self.open

    @property
    def body_size(self) -> float:
        return abs(
            self.close - self.open
        )

    @property
    def range(self) -> float:
        return self.high - self.low

    @classmethod
    def from_bybit(
        cls,
        symbol: str,
        interval: str,
        data: dict,
    ):

        return cls(
            symbol=symbol,
            interval=interval,
            timestamp=datetime.fromtimestamp(
                int(data["start"]) / 1000
            ),
            open=float(data["open"]),
            high=float(data["high"]),
            low=float(data["low"]),
            close=float(data["close"]),
            volume=float(data["volume"]),
            turnover=float(data["turnover"]),
        )

    @classmethod
    def from_series(
        cls,
        row: pd.Series,
        symbol: str,
        interval: str,
    ):

        return cls(
            symbol=symbol,
            interval=interval,
            timestamp=row["timestamp"],
            open=float(row["open"]),
            high=float(row["high"]),
            low=float(row["low"]),
            close=float(row["close"]),
            volume=float(row["volume"]),
            turnover=float(row["turnover"]),
        )

    @classmethod
    def from_dict(
        cls,
        symbol: str,
        interval: str,
        data: dict,
    ):

        return cls(
            symbol=symbol,
            interval=interval,
            timestamp=data["timestamp"],
            open=float(data["open"]),
            high=float(data["high"]),
            low=float(data["low"]),
            close=float(data["close"]),
            volume=float(data["volume"]),
            turnover=float(data["turnover"]),
        )