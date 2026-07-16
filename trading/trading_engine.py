from scanner.opportunity_manager import OpportunityManager
from portfolio.portfolio_manager import PortfolioManager


class TradingEngine:

    def __init__(
        self,
        scanner: OpportunityManager,
        portfolio: PortfolioManager,
    ):

        self.scanner = scanner
        self.portfolio = portfolio

    def scan(
        self,
        limit: int,
    ):

        return self.scanner.find(
            limit=limit,
        )