from execution.execution_coordinator import ExecutionCoordinator
from market.market_data_loader import MarketDataLoader
from portfolio.portfolio_manager import PortfolioManager


class OpportunityProcessor:

    def __init__(
        self,
        portfolio: PortfolioManager,
        execution: ExecutionCoordinator,
        market_loader: MarketDataLoader,
    ):

        self.portfolio = portfolio
        self.execution = execution
        self.market_loader = market_loader

    def process(
        self,
        opportunities,
        interval: str = "1",
    ) -> None:

        for opportunity in opportunities:

            symbol = opportunity.symbol.symbol

            series = self.market_loader.load(
                symbol=symbol,
                interval=interval,
                limit=200,
            )

            candle = series.last

            if candle is None:
                continue

            decision = self.portfolio.process_candle(
                candle
            )

            asset = self.portfolio.get_asset(
                symbol
            )

            self.execution.execute(
                engine=asset.engine,
                decision=decision,
            )