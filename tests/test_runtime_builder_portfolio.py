from runtime.trading_runtime_builder import (
    TradingRuntimeBuilder,
)

from exchange.paper_exchange import (
    PaperExchange,
)

from strategies.trend.sma_crossover import (
    SMACrossover,
)

print(
    "========== BUILDER PORTFOLIO ==========\n"
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

portfolio = builder.build_portfolio()

print(
    portfolio.count
)

for symbol in portfolio.symbols:

    print(symbol)