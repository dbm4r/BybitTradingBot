from exchange.exchange_symbol import ExchangeSymbol

from scanner.analysis_result import AnalysisResult
from scanner.filters.base_filter import BaseFilter
from scanner.filters.filter_pipeline import (
    FilterPipeline,
)


class PassFilter(BaseFilter):

    def filter(
        self,
        analysis,
    ):

        return True


class FailFilter(BaseFilter):

    def filter(
        self,
        analysis,
    ):

        return False


symbol = ExchangeSymbol(
    symbol="BTCUSDT",
    base_coin="BTC",
    quote_coin="USDT",
    status="Trading",
    tick_size=0.1,
    qty_step=0.001,
    min_order_qty=0.001,
    max_order_qty=1000,
    is_tradable=True,
)

analysis = AnalysisResult(
    symbol=symbol,
    regime=None,
)

print("========== FILTER PIPELINE ==========\n")


pipeline = FilterPipeline(
    [
        PassFilter(),
        PassFilter(),
    ]
)

print(
    pipeline.filter(
        analysis
    )
)

pipeline = FilterPipeline(
    [
        PassFilter(),
        FailFilter(),
        PassFilter(),
    ]
)

print(
    pipeline.filter(
        analysis
    )
)