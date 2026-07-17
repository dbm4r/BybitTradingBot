from exchange.paper_exchange import PaperExchange

from runtime.trading_runtime_builder import (
    TradingRuntimeBuilder,
)

print(
    "========== BUILDER MARKET ==========\n"
)

builder = (
    TradingRuntimeBuilder()
    .exchange(
        PaperExchange(
            symbol="BTCUSDT"
        )
    )
)

service = builder.build_market_data_service()

loader = builder.build_market_data_loader()

print(service.__class__.__name__)

print(loader.__class__.__name__)

print(
    loader.service is service
)

print(
    loader.exchange.__class__.__name__
)