from collections.abc import Iterator

from models.candle import Candle


class CandleSeries:
    def __init__(self):
        self._candles: list[Candle] = []

    def add(self, candle: Candle) -> None:
        self._candles.append(candle)

    @property
    def candles(self) -> tuple[Candle, ...]:
        return tuple(self._candles)

    @property
    def last(self) -> Candle | None:
        if not self._candles:
            return None
        return self._candles[-1]

    def last_n(self, n: int) -> list[Candle]:
        return self._candles[-n:]

    def __len__(self) -> int:
        return len(self._candles)

    def __getitem__(self, index: int) -> Candle:
        return self._candles[index]

    def __iter__(self) -> Iterator[Candle]:
        return iter(self._candles)
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
    def first(self) -> Candle | None:
        if not self._candles:
            return None
        return self._candles[0]


    @property
    def is_empty(self) -> bool:
        return len(self._candles) == 0


    @property
    def count(self) -> int:
        return len(self._candles)