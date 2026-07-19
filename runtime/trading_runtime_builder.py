from exchange.exchange import Exchange
from market.market_data_provider import MarketDataProvider
from runtime.cycle.opportunity_processor import OpportunityProcessor
from runtime.cycle.trading_context import TradingContext
from runtime.cycle.trading_cycle import TradingCycle
from scanner.market_scanner import MarketScanner
from strategies.framework.base_strategy import BaseStrategy
from market.market_data_loader import MarketDataLoader
from market.market_data_service import MarketDataService
from scanner.universe import SymbolUniverse
from scanner.symbol_analyzer import SymbolAnalyzer
from portfolio.portfolio_manager import PortfolioManager
from execution.execution_coordinator import ExecutionCoordinator


class TradingRuntimeBuilder:

    def __init__(self):

        self._exchange: Exchange | None = None

        self._market_data: MarketDataProvider | None = None

        self._strategy: BaseStrategy | None = None

        self._symbols: list[str] = []

        self._interval = "1"

        self._market_data_service = None
        self._market_data_loader = None
        self._universe = None
        self._symbol_analyzer = None
        self._market_scanner = None
        self._portfolio_manager = None
        self._execution = None
        self._processor = None

    def exchange(
        self,
        exchange: Exchange,
    ):

        self._exchange = exchange

        return self

    def market_data(
        self,
        provider: MarketDataProvider,
    ):

        self._market_data = provider

        return self

    def strategy(
        self,
        strategy: BaseStrategy,
    ):

        self._strategy = strategy

        return self

    def symbols(
        self,
        symbols: list[str],
    ):

        self._symbols = list(symbols)

        return self

    def interval(
        self,
        interval: str,
    ):

        self._interval = interval

        return self

    def build_exchange(
        self,
    ) -> Exchange:

        return self._exchange

    def build_market_data_provider(
        self,
    ) -> MarketDataProvider:

        return self._market_data

    def build_market_data_service(
        self,
    ) -> MarketDataService:

        if self._market_data_service is None:

            self._market_data_service = (
                MarketDataService()
            )

        return self._market_data_service

    def build_market_data_loader(
        self,
    ) -> MarketDataLoader:

        if self._market_data_loader is None:

            self._market_data_loader = (
                MarketDataLoader(
                    provider=self.build_market_data_provider(),
                    service=self.build_market_data_service(),
                )
            )

        return self._market_data_loader

    def build_symbol_universe(
        self,
    ) -> SymbolUniverse:

        if self._universe is None:

            self._universe = SymbolUniverse()

            available = {
                symbol.symbol: symbol
                for symbol in self.build_market_data_provider().get_symbols()
            }

            for name in self._symbols:

                symbol = available.get(name)

                if symbol is None:
                    raise ValueError(
                        f"Unknown symbol: {name}"
                    )

                self._universe.add(symbol)

        return self._universe

    def build_symbol_analyzer(
        self,
    ) -> SymbolAnalyzer:

        if self._symbol_analyzer is None:

            self._symbol_analyzer = (
                SymbolAnalyzer(
                    provider=self.build_market_data_provider(),
                )
            )

        return self._symbol_analyzer

    def build_market_scanner(
        self,
    ) -> MarketScanner:

        if self._market_scanner is None:

            self._market_scanner = (
                MarketScanner(
                    universe=self.build_symbol_universe(),
                    analyzer=self.build_symbol_analyzer(),
                )
            )

        return self._market_scanner

    def build_portfolio(
        self,
    ) -> PortfolioManager:

        if self._portfolio_manager is None:

            self._portfolio_manager = (
                PortfolioManager()
            )

            for symbol in self._symbols:

                self._portfolio_manager.register_asset(
                    symbol=symbol,
                    strategy=self._strategy,
                    interval=self._interval,
                )

        return self._portfolio_manager

    def build_execution(
        self,
    ) -> ExecutionCoordinator:

        if self._execution is None:

            self._execution = (
                ExecutionCoordinator()
            )

        return self._execution

    def build_processor(
        self,
    ) -> OpportunityProcessor:

        if self._processor is None:

            self._processor = (
                OpportunityProcessor(
                    portfolio=self.build_portfolio(),
                    execution=self.build_execution(),
                    market_loader=self.build_market_data_loader(),
                )
            )

        return self._processor

    def build_context(
        self,
    ) -> TradingContext:

        return TradingContext(
            scanner=self.build_market_scanner(),
            processor=self.build_processor(),
        )

    def build_cycle(
        self,
    ) -> TradingCycle:

        return TradingCycle(
            context=self.build_context(),
        )

    def build(
        self,
    ) -> TradingCycle:

        return self.build_cycle()