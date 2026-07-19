from abc import ABC, abstractmethod

from exchange.exchange_symbol import ExchangeSymbol


class MarketDataProvider(ABC):

    @abstractmethod
    def get_symbols(
        self,
    ) -> list[ExchangeSymbol]:
        pass

    @abstractmethod
    def get_candles(
        self,
        symbol: str,
        interval: str,
        limit: int = 200,
    ):
        pass