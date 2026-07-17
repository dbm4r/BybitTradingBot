from exchange.paper_exchange import PaperExchange

from runtime.trading_runtime_builder import (
    TradingRuntimeBuilder,
)

from strategies.trend.sma_crossover import (
    SMACrossover,
)

print(
    "========== BUILDER PROCESSOR ==========\n"
)

builder = (
    TradingRuntimeBuilder()
    .exchange(
        PaperExchange(
            symbol="BTCUSDT",
        )
    )
    .strategy(
        SMACrossover()
    )
    .symbols(
        [
            "BTCUSDT",
            "ETHUSDT",
        ]
    )
)

processor = builder.build_processor()

print(
    processor.__class__.__name__
)

print(
    processor is builder.build_processor()
)