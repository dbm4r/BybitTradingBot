from datetime import datetime

from backtesting.portfolio import Portfolio

from portfolio.portfolio_statistics import (
    PortfolioStatistics,
)
from portfolio.portfolio_performance import (
    PortfolioPerformance,
)
from portfolio.portfolio_report import (
    PortfolioReport,
)

portfolio = Portfolio(10000)

statistics = PortfolioStatistics.from_portfolio(
    portfolio,
    total_fees=25,
)

performance = PortfolioPerformance.from_statistics(
    initial_balance=portfolio.initial_balance,
    statistics=statistics,
)

report = PortfolioReport(
    timestamp=datetime.now(),
    statistics=statistics,
    performance=performance,
)

print("========== PORTFOLIO REPORT ==========\n")

print(f"Time              : {report.timestamp}")
print(f"Portfolio Value   : ${report.portfolio_value:,.2f}")
print(f"Cash              : ${report.cash:,.2f}")
print(f"Invested Capital  : ${report.invested_capital:,.2f}")
print(f"Open Positions    : {report.open_positions}")
print(f"Return            : {report.total_return_percent:.2f}%")
print(f"Utilization       : {report.capital_utilization_percent:.2f}%")
print(f"Fees              : {report.fee_percent:.2f}%")