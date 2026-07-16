from exchange.exchange_symbol import ExchangeSymbol

from scanner.universe import SymbolUniverse
from scanner.market_scanner import MarketScanner
from scanner.symbol_analyzer import SymbolAnalyzer


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


print("========== MARKET SCANNER ==========\n")


universe = SymbolUniverse()


btc = ExchangeSymbol(
    symbol="BTCUSDT",
    base_coin="BTC",
    quote_coin="USDT",
    status="Trading",
    tick_size=0.1,
    qty_step=0.001,
    min_order_qty=0.001,
    max_order_qty=1000,
    is_tradable=True,
)


eth = ExchangeSymbol(
    symbol="ETHUSDT",
    base_coin="ETH",
    quote_coin="USDT",
    status="Trading",
    tick_size=0.01,
    qty_step=0.001,
    min_order_qty=0.001,
    max_order_qty=1000,
    is_tradable=True,
)


universe.add(btc)
universe.add(eth)


analyzer = SymbolAnalyzer(
    MockExchange()
)


scanner = MarketScanner(
    universe=universe,
    analyzer=analyzer,
)


results = scanner.scan()


for result in results:

    print(
        result.symbol.symbol,
        result.score,
    )