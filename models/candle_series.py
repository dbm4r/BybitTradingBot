from collections import deque
from collections.abc import Iterable, Iterator

from models.candle import Candle


class CandleSeries:
    def __init__(
        self,
        symbol: str,
        interval: str,
        candles: Iterable[Candle] | None = None,
        max_size: int = 5000,
    ):
        self.symbol = symbol
        self.interval = interval
        self.max_size = max_size
        self._candles = deque(candles or [], maxlen=max_size)

    def add(self, candle: Candle) -> None:
        if not isinstance(candle, Candle):
            raise TypeError("Expected a Candle instance.")

        if candle.symbol != self.symbol:
            raise ValueError(
                f"Expected symbol '{self.symbol}', got '{candle.symbol}'."
            )

        if candle.interval != self.interval:
            raise ValueError(
                f"Expected interval '{self.interval}', got '{candle.interval}'."
            )

        if candle.low > candle.high:
            raise ValueError("Candle low cannot be greater than candle high.")

        if not (candle.low <= candle.open <= candle.high):
            raise ValueError("Open price is outside candle range.")

        if not (candle.low <= candle.close <= candle.high):
            raise ValueError("Close price is outside candle range.")

        if self.last and candle.timestamp == self.last.timestamp:
            raise ValueError("Duplicate candle timestamp.")

        self._candles.append(candle)

    def update_last(self, candle: Candle) -> None:
        if not isinstance(candle, Candle):
            raise TypeError("Expected a Candle instance.")

        if candle.symbol != self.symbol:
            raise ValueError(
                f"Expected symbol '{self.symbol}', got '{candle.symbol}'."
            )

        if candle.interval != self.interval:
            raise ValueError(
                f"Expected interval '{self.interval}', got '{candle.interval}'."
            )

        if candle.low > candle.high:
            raise ValueError("Candle low cannot be greater than candle high.")

        if not (candle.low <= candle.open <= candle.high):
            raise ValueError("Open price is outside candle range.")

        if not (candle.low <= candle.close <= candle.high):
            raise ValueError("Close price is outside candle range.")

        if self.is_empty:
            self._candles.append(candle)
        else:
            self._candles[-1] = candle

    @property
    def candles(self) -> tuple[Candle, ...]:
        return tuple(self._candles)

    @property
    def first(self) -> Candle | None:
        if self.is_empty:
            return None
        return self._candles[0]

    @property
    def last(self) -> Candle | None:
        if self.is_empty:
            return None
        return self._candles[-1]

    def last_n(self, n: int) -> tuple[Candle, ...]:
        return tuple(list(self._candles)[-n:])

    @property
    def open_prices(self) -> list[float]:
        return [c.open for c in self._candles]

    @property
    def high_prices(self) -> list[float]:
        return [c.high for c in self._candles]

    @property
    def low_prices(self) -> list[float]:
        return [c.low for c in self._candles]

    @property
    def close_prices(self) -> list[float]:
        return [c.close for c in self._candles]

    @property
    def volumes(self) -> list[float]:
        return [c.volume for c in self._candles]

    @property
    def last_open(self) -> float | None:
        return None if self.last is None else self.last.open

    @property
    def last_high(self) -> float | None:
        return None if self.last is None else self.last.high

    @property
    def last_low(self) -> float | None:
        return None if self.last is None else self.last.low

    @property
    def last_close(self) -> float | None:
        return None if self.last is None else self.last.close

    @property
    def last_volume(self) -> float | None:
        return None if self.last is None else self.last.volume

    @property
    def start_time(self):
        return None if self.first is None else self.first.timestamp

    @property
    def end_time(self):
        return None if self.last is None else self.last.timestamp

    @property
    def is_empty(self) -> bool:
        return len(self._candles) == 0

    @property
    def count(self) -> int:
        return len(self._candles)

    def __len__(self) -> int:
        return len(self._candles)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return tuple(list(self._candles)[index])
        return list(self._candles)[index]

    def __iter__(self) -> Iterator[Candle]:
        return iter(self._candles)