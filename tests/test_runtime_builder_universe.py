from exchange.paper_exchange import PaperExchange
from runtime.trading_runtime_builder import (
    TradingRuntimeBuilder,
)

print(
    "========== BUILDER UNIVERSE ==========\n"
)

builder = (
    TradingRuntimeBuilder()
    .exchange(
        PaperExchange(
            symbol="BTCUSDT"
        )
    )
    .symbols(
        [
            "BTCUSDT",
            "ETHUSDT",
            "SOLUSDT",
        ]
    )
)

universe = builder.build_symbol_universe()

print(
    universe.count
)

for symbol in universe:

    print(
        symbol.symbol
    )