from exchange.bybit_exchange import BybitExchange

print("========== EXCHANGE SYMBOLS ==========\n")

exchange = BybitExchange(
    api_key="xdRbOU4VvVZcwxOcEG",
    api_secret="s798S41QJlK10r3zcyPIWxD7p9Tjo70PNrpa",
    base_url="https://api-demo.bybit.com",
    symbol="BTCUSDT",
)

symbols = exchange.get_symbols()

print(type(symbols).__name__)
print(len(symbols))

btc = next(
    s for s in symbols
    if s.symbol == "BTCUSDT"
)

print(btc.symbol)
print(btc.tick_size)
print(btc.qty_step)
print(btc.is_tradable)