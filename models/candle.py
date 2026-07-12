from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
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
        return abs(self.close - self.open)

    @property
    def range(self) -> float:
        return self.high - self.low

    @classmethod
    def from_bybit(cls, symbol: str, interval: str, data: dict):
        return cls(
            symbol=symbol,
            interval=interval,
            timestamp=datetime.fromtimestamp(int(data["start"]) / 1000),
            open=float(data["open"]),
            high=float(data["high"]),
            low=float(data["low"]),
            close=float(data["close"]),
            volume=float(data["volume"]),
            turnover=float(data["turnover"]),
        )