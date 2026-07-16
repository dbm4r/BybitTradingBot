from exchange.exchange_symbol import ExchangeSymbol

from scanner.analysis_result import AnalysisResult
from scanner.ranking.score_ranker import ScoreRanker


print("========== SCORE RANKER ==========\n")


btc = AnalysisResult(
    symbol=ExchangeSymbol(
        symbol="BTCUSDT",
        base_coin="BTC",
        quote_coin="USDT",
        status="Trading",
        tick_size=0.1,
        qty_step=0.001,
        min_order_qty=0.001,
        max_order_qty=1000,
        is_tradable=True,
    ),
    regime=None,
    score=82,
)

eth = AnalysisResult(
    symbol=ExchangeSymbol(
        symbol="ETHUSDT",
        base_coin="ETH",
        quote_coin="USDT",
        status="Trading",
        tick_size=0.01,
        qty_step=0.001,
        min_order_qty=0.001,
        max_order_qty=1000,
        is_tradable=True,
    ),
    regime=None,
    score=95,
)

sol = AnalysisResult(
    symbol=ExchangeSymbol(
        symbol="SOLUSDT",
        base_coin="SOL",
        quote_coin="USDT",
        status="Trading",
        tick_size=0.01,
        qty_step=0.01,
        min_order_qty=0.01,
        max_order_qty=100000,
        is_tradable=True,
    ),
    regime=None,
    score=74,
)

ranker = ScoreRanker()

results = ranker.rank(
    [
        btc,
        sol,
        eth,
    ]
)

for result in results:

    print(
        result.symbol.symbol,
        result.score,
    )