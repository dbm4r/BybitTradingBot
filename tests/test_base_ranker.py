from exchange.exchange_symbol import ExchangeSymbol

from scanner.analysis_result import AnalysisResult
from scanner.ranking.base_ranker import BaseRanker


class DummyRanker(BaseRanker):

    def rank(
        self,
        analyses,
    ):

        return analyses


print("========== BASE RANKER ==========\n")


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
    score=90,
)


ranker = DummyRanker()

results = ranker.rank(
    [analysis]
)

print(
    results[0].symbol.symbol
)

print(
    results[0].score
)