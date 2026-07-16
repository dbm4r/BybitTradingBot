from datetime import datetime

from backtesting.portfolio import Portfolio
from portfolio.portfolio_statistics import PortfolioStatistics
from portfolio.portfolio_performance import PortfolioPerformance
from portfolio.portfolio_report import PortfolioReport
from portfolio.portfolio_formatter import PortfolioFormatter

portfolio = Portfolio(10000)

statistics = PortfolioStatistics.from_portfolio(
    portfolio=portfolio,
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

print(
    PortfolioFormatter.format(
        report
    )
)