from exchange.exchange_symbol import ExchangeSymbol

from scanner.analysis_result import AnalysisResult
from scanner.opportunity_selector import OpportunitySelector


def create(symbol: str, score: float):

    return AnalysisResult(
        symbol=ExchangeSymbol(
            symbol=symbol,
            base_coin=symbol[:-4],
            quote_coin="USDT",
            status="Trading",
            tick_size=0.1,
            qty_step=0.001,
            min_order_qty=0.001,
            max_order_qty=1000,
            is_tradable=True,
        ),
        regime=None,
        score=score,
    )


print("========== OPPORTUNITY SELECTOR ==========\n")


selector = OpportunitySelector()

results = selector.select(
    [
        create("BTCUSDT", 95),
        create("ETHUSDT", 90),
        create("SOLUSDT", 80),
        create("XRPUSDT", 70),
    ],
    limit=2,
)

for result in results:

    print(
        result.symbol.symbol,
        result.score,
    )