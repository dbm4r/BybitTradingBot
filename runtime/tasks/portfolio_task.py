from portfolio.portfolio_manager import PortfolioManager
from runtime.runtime_task import RuntimeTask


class PortfolioTask(RuntimeTask):

    def __init__(
        self,
        portfolio: PortfolioManager,
    ):

        self.portfolio = portfolio

    def run(
        self,
    ) -> None:

        self.portfolio.process()