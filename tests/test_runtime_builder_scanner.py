from exchange.paper_exchange import PaperExchange

from runtime.trading_runtime_builder import (
    TradingRuntimeBuilder,
)

print(
    "========== BUILDER SCANNER ==========\n"
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

scanner = builder.build_market_scanner()

print(
    scanner.__class__.__name__
)

print(
    scanner.universe.count
)

print(
    scanner.analyzer.__class__.__name__
)

print(
    scanner is builder.build_market_scanner()
)