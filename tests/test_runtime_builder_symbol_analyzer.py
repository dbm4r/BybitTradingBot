from exchange.paper_exchange import PaperExchange

from runtime.trading_runtime_builder import (
    TradingRuntimeBuilder,
)

print(
    "========== BUILDER SYMBOL ANALYZER ==========\n"
)

builder = (
    TradingRuntimeBuilder()
    .exchange(
        PaperExchange(
            symbol="BTCUSDT"
        )
    )
)

analyzer = builder.build_symbol_analyzer()

print(
    analyzer.__class__.__name__
)

print(
    analyzer.exchange.__class__.__name__
)

print(
    analyzer is builder.build_symbol_analyzer()
)