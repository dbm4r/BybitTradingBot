from scanner.symbol_loader import SymbolLoader

print("========== SYMBOL LOADER ==========\n")

response = {
    "result": {
        "list": [
            {
                "symbol": "BTCUSDT",
                "baseCoin": "BTC",
                "quoteCoin": "USDT",
                "status": "Trading",
                "priceFilter": {
                    "tickSize": "0.10",
                },
                "lotSizeFilter": {
                    "qtyStep": "0.001",
                    "minOrderQty": "0.001",
                    "maxOrderQty": "1000",
                },
            },
            {
                "symbol": "ETHUSDT",
                "baseCoin": "ETH",
                "quoteCoin": "USDT",
                "status": "Trading",
                "priceFilter": {
                    "tickSize": "0.01",
                },
                "lotSizeFilter": {
                    "qtyStep": "0.001",
                    "minOrderQty": "0.001",
                    "maxOrderQty": "1000",
                },
            },
        ]
    }
}

symbols = SymbolLoader.load(response)

print("Count:")
print(len(symbols))
print()

for symbol in symbols:
    print(symbol.symbol)
    print(symbol.base_coin)
    print(symbol.quote_coin)
    print(symbol.tick_size)
    print(symbol.qty_step)
    print()