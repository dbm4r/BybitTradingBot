from scanner.universe_manager import UniverseManager


class MockExchange:

    def get_symbols(self):

        return {
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
                    {
                        "symbol": "OLDCOINUSDT",
                        "baseCoin": "OLD",
                        "quoteCoin": "USDT",
                        "status": "Settled",
                        "priceFilter": {
                            "tickSize": "0.01",
                        },
                        "lotSizeFilter": {
                            "qtyStep": "1",
                            "minOrderQty": "1",
                            "maxOrderQty": "1000",
                        },
                    },
                ]
            }
        }


print("========== UNIVERSE MANAGER ==========\n")

manager = UniverseManager(
    MockExchange()
)

universe = manager.load()

print("Count:")
print(universe.count)
print()

print("Symbols:")

for symbol in universe:
    print(symbol.symbol)