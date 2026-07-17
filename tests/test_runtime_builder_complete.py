from exchange.paper_exchange import PaperExchange

from runtime.trading_runtime_builder import (
    TradingRuntimeBuilder,
)

from runtime.cycle.trading_cycle import TradingCycle

from strategies.trend.sma_crossover import (
    SMACrossover,
)

print(
    "========== COMPLETE BUILDER ==========\n"
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
            "SOLUSDT",
        ]
    )
)

cycle = builder.build()

print(
    isinstance(
        cycle,
        TradingCycle,
    )
)

print(
    cycle.context.scanner.__class__.__name__
)

print(
    cycle.context.processor.__class__.__name__
)