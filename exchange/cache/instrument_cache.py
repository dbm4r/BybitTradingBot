class InstrumentCache:

    def __init__(self):

        self._cache = {}

    def get(
        self,
        symbol: str,
    ):

        return self._cache.get(
            symbol,
        )

    def put(
        self,
        instrument,
    ):

        self._cache[
            instrument.symbol
        ] = instrument

    def contains(
        self,
        symbol: str,
    ) -> bool:

        return symbol in self._cache

    def clear(
        self,
    ):

        self._cache.clear()

    def values(
        self,
    ):

        return tuple(
            self._cache.values()
        )

    def size(
        self,
    ):

        return len(
            self._cache
        )