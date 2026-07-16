from dataclasses import dataclass

from exchange.exchange_symbol import ExchangeSymbol
from market.regime_result import RegimeResult


@dataclass(slots=True)
class AnalysisResult:

    symbol: ExchangeSymbol

    regime: RegimeResult

    score: float = 0.0

    passed: bool = True

    reason: str | None = None