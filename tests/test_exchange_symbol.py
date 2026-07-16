from exchange.exchange_symbol import ExchangeSymbol

print("========== EXCHANGE SYMBOL ==========\n")

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

print(symbol.symbol)
print(symbol.base_coin)
print(symbol.quote_coin)
print(symbol.status)
print(symbol.tick_size)
print(symbol.qty_step)
print(symbol.min_order_qty)
print(symbol.max_order_qty)
print(symbol.is_tradable)