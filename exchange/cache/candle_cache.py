from models.candle_series import CandleSeries


class CandleCache:

    def __init__(self):

        self._cache: dict[
            tuple[str, str],
            CandleSeries,
        ] = {}

    def get(
        self,
        symbol: str,
        interval: str,
    ) -> CandleSeries | None:

        return self._cache.get(
            (symbol, interval),
        )

    def put(
        self,
        series: CandleSeries,
    ) -> None:

        self._cache[
            (
                series.symbol,
                series.interval,
            )
        ] = series

    def contains(
        self,
        symbol: str,
        interval: str,
    ) -> bool:

        return (
            symbol,
            interval,
        ) in self._cache

    def remove(
        self,
        symbol: str,
        interval: str,
    ) -> None:

        self._cache.pop(
            (
                symbol,
                interval,
            ),
            None,
        )

    def clear(
        self,
    ) -> None:

        self._cache.clear()

    def values(
        self,
    ) -> tuple[CandleSeries, ...]:

        return tuple(
            self._cache.values()
        )

    def size(
        self,
    ) -> int:

        return len(
            self._cache
        )