from scanner.filters.base_filter import BaseFilter
from scanner.analysis_result import AnalysisResult
from exchange.exchange_symbol import ExchangeSymbol


class DummyFilter(BaseFilter):

    def filter(
        self,
        analysis,
    ):

        return True


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


dummy = DummyFilter()


print("========== BASE FILTER ==========\n")

print(
    dummy.filter(
        analysis
    )
)