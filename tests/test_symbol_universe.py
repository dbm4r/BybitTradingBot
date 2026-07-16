from exchange.exchange_symbol import ExchangeSymbol
from scanner.universe import SymbolUniverse

print("========== SYMBOL UNIVERSE ==========\n")

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

sol = ExchangeSymbol(
    symbol="SOLUSDT",
    base_coin="SOL",
    quote_coin="USDT",
    status="Trading",
    tick_size=0.001,
    qty_step=0.01,
    min_order_qty=0.01,
    max_order_qty=100000,
    is_tradable=True,
)

universe.add(btc)
universe.add(eth)
universe.add(sol)

print("Count:")
print(universe.count)
print()

print("Symbols:")

for symbol in universe:
    print(symbol.symbol)

print()

print("BTC Exists:")
print(universe.exists("BTCUSDT"))
print()

print("ETH:")
print(universe.get("ETHUSDT").symbol)
print()

universe.remove("ETHUSDT")

print("After Removing ETH:")

for symbol in universe:
    print(symbol.symbol)

print()

print("Final Count:")
print(universe.count)