from unittest.mock import Mock

from runtime.trading_runtime_builder import (
    TradingRuntimeBuilder,
)


def test_builder_stores_market_data():

    provider = Mock()

    builder = (
        TradingRuntimeBuilder()
        .market_data(provider)
    )

    assert (
        builder.build_market_data_provider()
        is provider
    )