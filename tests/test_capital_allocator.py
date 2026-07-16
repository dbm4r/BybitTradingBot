from backtesting.portfolio import Portfolio
from portfolio.capital_allocator import (
    CapitalAllocator,
)
from portfolio.portfolio_constraints import (
    PortfolioConstraints,
)

portfolio = Portfolio(10000)

allocator = CapitalAllocator(
    PortfolioConstraints(
        max_symbol_allocation=0.25,
    )
)

allocation = allocator.allocate(
    portfolio
)

print(
    "========== CAPITAL ALLOCATOR ==========\n"
)

print(
    f"Cash        : ${portfolio.cash:,.2f}"
)

print(
    f"Allocation  : ${allocation:,.2f}"
)