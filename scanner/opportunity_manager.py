from scanner.market_scanner import MarketScanner
from scanner.opportunity_selector import OpportunitySelector
from scanner.scanner_settings import ScannerSettings


class OpportunityManager:

    def __init__(
        self,
        scanner: MarketScanner,
        settings: ScannerSettings | None = None,
    ):

        self.scanner = scanner
        self.selector = OpportunitySelector()

        self.settings = (
            settings
            or ScannerSettings()
        )

    def find(
        self,
        limit: int | None = None,
    ):

        opportunities = self.scanner.scan()

        if limit is None:

            limit = self.settings.max_opportunities

        return self.selector.select(
            opportunities,
            limit,
        )