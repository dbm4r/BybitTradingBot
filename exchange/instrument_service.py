from bybit.parsers.instrument_parser import (
    BybitInstrumentParser,
)

from exchange.cache.instrument_cache import (
    InstrumentCache,
)


class InstrumentService:

    def __init__(
        self,
        client,
    ):

        self.client = client

        self.cache = InstrumentCache()

    def get(
        self,
        symbol: str,
    ):

        instrument = self.cache.get(
            symbol,
        )

        if instrument is not None:
            return instrument

        response = self.client.market.get_instruments(
            symbol=symbol,
        )

        item = response["result"]["list"][0]

        instrument = BybitInstrumentParser.parse(
            item,
        )

        self.cache.put(
            instrument,
        )

        return instrument

    def clear_cache(
        self,
    ):

        self.cache.clear()

    def cache_size(
        self,
    ):

        return self.cache.size()