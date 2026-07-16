from exchange.exchange_symbol import ExchangeSymbol
from scanner.opportunity import Opportunity

print("========== OPPORTUNITY ==========\n")

btc = ExchangeSymbol(
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

opportunity = Opportunity(
    symbol=btc,
    score=92.5,
    passed=True,
    reason="Strong trend",
)

print(opportunity.symbol.symbol)
print(opportunity.score)
print(opportunity.passed)
print(opportunity.reason)