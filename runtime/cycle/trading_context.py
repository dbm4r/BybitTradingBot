from dataclasses import dataclass

from runtime.cycle.opportunity_processor import (
    OpportunityProcessor,
)
from scanner.market_scanner import MarketScanner


@dataclass(slots=True)
class TradingContext:

    scanner: MarketScanner

    processor: OpportunityProcessor