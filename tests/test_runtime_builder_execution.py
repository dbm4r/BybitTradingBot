from runtime.trading_runtime_builder import (
    TradingRuntimeBuilder,
)

print(
    "========== BUILDER EXECUTION ==========\n"
)

builder = TradingRuntimeBuilder()

execution = builder.build_execution()

print(
    execution.__class__.__name__
)

print(
    execution is builder.build_execution()
)