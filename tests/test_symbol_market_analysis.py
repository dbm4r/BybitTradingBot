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


print("========== SYMBOL MARKET ANALYSIS ==========\n")

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

analysis = analyzer.analyze_market(
    symbol=symbol,
    interval="1",
)

print(analysis.regime)

print()

print("Trend:")
print(analysis.score.trend)

print()

print("Volatility:")
print(analysis.score.volatility)

print()

print("Liquidity:")
print(analysis.score.liquidity)

print()

print("Confidence:")
print(analysis.score.confidence)

print()

print("Overall:")
print(analysis.score.overall)