from dataclasses import dataclass

from exchange.exchange_symbol import ExchangeSymbol


@dataclass(slots=True)
class Opportunity:

    symbol: ExchangeSymbol

    score: float = 0.0

    passed: bool = True

    reason: str | None = None