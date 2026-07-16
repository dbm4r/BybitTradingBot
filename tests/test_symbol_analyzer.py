from exchange.exchange_symbol import ExchangeSymbol
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
                        "1720000200000",
                        "65000",
                        "65200",
                        "64800",
                        "65100",
                        "120",
                        "7800000",
                    ],
                    [
                        "1720000140000",
                        "64800",
                        "65100",
                        "64700",
                        "65000",
                        "100",
                        "6500000",
                    ],
                ]
            }
        }


print("========== SYMBOL ANALYZER ==========\n")

symbol = ExchangeSymbol(
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

analyzer = SymbolAnalyzer(
    MockExchange()
)

series = analyzer.load_candles(
    symbol,
    interval="1",
)

print(series.symbol)
print(series.interval)
print(len(series.candles))

print()

for candle in series.candles:

    print(
        candle.close
    )