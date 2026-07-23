from dataclasses import dataclass

from runtime.cycle.opportunity_processor import (
    OpportunityProcessor,
)

from scanner.market_scanner import (
    MarketScanner,
)

from scanner.opportunity import (
    Opportunity,
)


@dataclass(slots=True)
class TradingContext:

    scanner: MarketScanner

    processor: OpportunityProcessor

    opportunities: list[
        Opportunity
    ] | None = None