from backtesting.portfolio import Portfolio
from portfolio.portfolio_constraints import (
    PortfolioConstraints,
)


class CapitalAllocator:

    def __init__(
        self,
        constraints: PortfolioConstraints,
    ):

        self.constraints = constraints

    def allocate(
        self,
        portfolio: Portfolio,
    ) -> float:

        allocation = (
            portfolio.total_value(
                symbol="",
                current_price=0,
            )
            * self.constraints.max_symbol_allocation
        )

        return min(
            allocation,
            portfolio.cash,
        )