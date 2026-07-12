from models.candle import Candle
from models.candle_series import CandleSeries


class MarketDataService:
    def __init__(self):
        self._series: dict[tuple[str, str], CandleSeries] = {}

    @staticmethod
    def _key(symbol: str, interval: str) -> tuple[str, str]:
        return symbol, interval

    def create_series(
        self,
        symbol: str,
        interval: str,
        max_size: int = 5000,
    ) -> CandleSeries:
        key = self._key(symbol, interval)

        if key not in self._series:
            self._series[key] = CandleSeries(
                symbol=symbol,
                interval=interval,
                max_size=max_size,
            )

        return self._series[key]

    def has_series(
        self,
        symbol: str,
        interval: str,
    ) -> bool:
        return self._key(symbol, interval) in self._series

    def get_series(
        self,
        symbol: str,
        interval: str,
    ) -> CandleSeries | None:
        return self._series.get(
            self._key(symbol, interval)
        )

    def remove_series(
        self,
        symbol: str,
        interval: str,
    ) -> None:
        self._series.pop(
            self._key(symbol, interval),
            None,
        )

    def clear(self) -> None:
        self._series.clear()

    def add_candle(
        self,
        candle: Candle,
    ) -> None:
        if not isinstance(candle, Candle):
            raise TypeError("Expected a Candle instance.")

        series = self.get_series(
            candle.symbol,
            candle.interval,
        )

        if series is None:
            series = self.create_series(
                candle.symbol,
                candle.interval,
            )

        series.add(candle)

    def update_last_candle(
        self,
        candle: Candle,
    ) -> None:
        if not isinstance(candle, Candle):
            raise TypeError("Expected a Candle instance.")

        series = self.get_series(
            candle.symbol,
            candle.interval,
        )

        if series is None:
            series = self.create_series(
                candle.symbol,
                candle.interval,
            )

        series.update_last(candle)

    def get_last_candle(
        self,
        symbol: str,
        interval: str,
    ) -> Candle | None:
        series = self.get_series(
            symbol,
            interval,
        )

        if series is None:
            return None

        return series.last

    def get_first_candle(
        self,
        symbol: str,
        interval: str,
    ) -> Candle | None:
        series = self.get_series(
            symbol,
            interval,
        )

        if series is None:
            return None

        return series.first

    def get_close_prices(
        self,
        symbol: str,
        interval: str,
    ) -> list[float]:
        series = self.get_series(
            symbol,
            interval,
        )

        return [] if series is None else series.close_prices

    def get_open_prices(
        self,
        symbol: str,
        interval: str,
    ) -> list[float]:
        series = self.get_series(
            symbol,
            interval,
        )

        return [] if series is None else series.open_prices

    def get_high_prices(
        self,
        symbol: str,
        interval: str,
    ) -> list[float]:
        series = self.get_series(
            symbol,
            interval,
        )

        return [] if series is None else series.high_prices

    def get_low_prices(
        self,
        symbol: str,
        interval: str,
    ) -> list[float]:
        series = self.get_series(
            symbol,
            interval,
        )

        return [] if series is None else series.low_prices

    def get_volumes(
        self,
        symbol: str,
        interval: str,
    ) -> list[float]:
        series = self.get_series(
            symbol,
            interval,
        )

        return [] if series is None else series.volumes

    @property
    def symbols(self) -> set[str]:
        return {
            symbol
            for symbol, _ in self._series.keys()
        }

    def intervals(
        self,
        symbol: str,
    ) -> list[str]:
        return sorted(
            interval
            for s, interval in self._series.keys()
            if s == symbol
        )

    @property
    def series_count(self) -> int:
        return len(self._series)

    @property
    def is_empty(self) -> bool:
        return len(self._series) == 0

    @property
    def series(self) -> tuple[CandleSeries, ...]:
        return tuple(self._series.values())

    def __len__(self) -> int:
        return len(self._series)

    def __contains__(
        self,
        item: tuple[str, str],
    ) -> bool:
        return item in self._series

    def __iter__(self):
        return iter(self._series.values())

    def __repr__(self) -> str:
        return (
            f"MarketDataService("
            f"series={self.series_count}, "
            f"symbols={len(self.symbols)})"
        )