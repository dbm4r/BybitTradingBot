from exchange.exchange_symbol import ExchangeSymbol
from scanner.scanner_settings import ScannerSettings
from scanner.market_scanner import MarketScanner
from scanner.opportunity_manager import OpportunityManager
from scanner.symbol_analyzer import SymbolAnalyzer
from scanner.universe import SymbolUniverse


class MockExchange:

    def get_candles(
        self,
        symbol,
        interval,
        limit,
    ):

        return {
            "result": {
                "list": [
                    [
                        "2",
                        "105",
                        "110",
                        "100",
                        "108",
                        "20",
                        "2160",
                    ],
                    [
                        "1",
                        "100",
                        "106",
                        "99",
                        "105",
                        "10",
                        "1050",
                    ],
                ]
            }
        }


print("========== OPPORTUNITY MANAGER ==========\n")


universe = SymbolUniverse()

for symbol in (
    "BTCUSDT",
    "ETHUSDT",
    "SOLUSDT",
):

    universe.add(
        ExchangeSymbol(
            symbol=symbol,
            base_coin=symbol[:-4],
            quote_coin="USDT",
            status="Trading",
            tick_size=0.1,
            qty_step=0.001,
            min_order_qty=0.001,
            max_order_qty=1000,
            is_tradable=True,
        )
    )


scanner = MarketScanner(
    universe=universe,
    analyzer=SymbolAnalyzer(
        MockExchange()
    ),
)

manager = OpportunityManager(
    scanner
)

manager = OpportunityManager(
    scanner,
    ScannerSettings(
        max_opportunities=2,
    ),
)

results = manager.find()

for result in results:

    print(
        result.symbol.symbol,
        result.score,
    )