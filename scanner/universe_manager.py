from exchange.exchange import Exchange
from scanner.symbol_loader import SymbolLoader
from scanner.universe import SymbolUniverse


class UniverseManager:

    def __init__(
        self,
        exchange: Exchange,
    ):

        self.exchange = exchange

        self.universe = SymbolUniverse()

    def load(self) -> SymbolUniverse:

        response = self.exchange.get_symbols()

        symbols = SymbolLoader.load(
            response
        )

        self.universe.clear()

        for symbol in symbols:

            if not symbol.is_tradable:
                continue

            self.universe.add(
                symbol
            )

        return self.universe

    @property
    def count(
        self,
    ) -> int:

        return self.universe.count