from exchange.exchange_symbol import ExchangeSymbol


class SymbolUniverse:

    def __init__(self):

        self._symbols: dict[str, ExchangeSymbol] = {}

    def add(
        self,
        symbol: ExchangeSymbol,
    ) -> None:

        self._symbols[symbol.symbol] = symbol

    def remove(
        self,
        symbol: str,
    ) -> None:

        self._symbols.pop(
            symbol,
            None,
        )

    def get(
        self,
        symbol: str,
    ) -> ExchangeSymbol:

        return self._symbols[symbol]

    def exists(
        self,
        symbol: str,
    ) -> bool:

        return symbol in self._symbols

    def clear(
        self,
    ) -> None:

        self._symbols.clear()

    @property
    def symbols(
        self,
    ) -> tuple[ExchangeSymbol, ...]:

        return tuple(
            self._symbols.values()
        )

    @property
    def count(
        self,
    ) -> int:

        return len(
            self._symbols
        )

    def __iter__(
        self):

        return iter(
            self._symbols.values()
        )