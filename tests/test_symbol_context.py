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


print("========== SYMBOL CONTEXT ==========\n")

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

context = analyzer.build_context(
    symbol=symbol,
    interval="1",
)

tf = context.get("1")

print(tf.timeframe)
print(tf.candles.symbol)
print(tf.candles.interval)
print(len(tf.candles))