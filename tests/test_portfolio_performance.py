from backtesting.portfolio import Portfolio

from portfolio.portfolio_statistics import (
    PortfolioStatistics,
)
from portfolio.portfolio_performance import (
    PortfolioPerformance,
)

portfolio = Portfolio(10000)

stats = PortfolioStatistics.from_portfolio(
    portfolio,
    total_fees=25,
)

performance = PortfolioPerformance.from_statistics(
    initial_balance=portfolio.initial_balance,
    statistics=stats,
)

print(
    "========== PORTFOLIO PERFORMANCE ==========\n"
)

print(
    f"Return      : {performance.total_return_percent:.2f}%"
)

print(
    f"Utilization : {performance.capital_utilization_percent:.2f}%"
)

print(
    f"Fees        : {performance.fee_percent:.2f}%"
)