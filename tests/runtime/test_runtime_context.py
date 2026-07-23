from unittest.mock import Mock

from runtime.cycle.trading_context import (
    TradingContext,
)


def test_trading_context_stores_dependencies():

    scanner = Mock()

    processor = Mock()

    context = TradingContext(
        scanner=scanner,
        processor=processor,
    )

    assert context.scanner is scanner

    assert context.processor is processor

    assert context.opportunities is None