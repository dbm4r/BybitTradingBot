from backtesting.portfolio import Portfolio
from portfolio.portfolio_statistics import (
    PortfolioStatistics,
)

portfolio = Portfolio(
    initial_balance=10000,
)

stats = PortfolioStatistics.from_portfolio(
    portfolio=portfolio,
    total_fees=12.50,
)

print(
    "========== PORTFOLIO STATISTICS ==========\n"
)

print(
    f"Cash               : ${stats.cash:,.2f}"
)

print(
    f"Invested Capital   : ${stats.invested_capital:,.2f}"
)

print(
    f"Portfolio Value    : ${stats.portfolio_value:,.2f}"
)

print(
    f"Open Positions     : {stats.open_positions}"
)

print(
    f"Realized PnL       : ${stats.realized_pnl:,.2f}"
)

print(
    f"Unrealized PnL     : ${stats.unrealized_pnl:,.2f}"
)

print(
    f"Total PnL          : ${stats.total_pnl:,.2f}"
)

print(
    f"Total Fees         : ${stats.total_fees:,.2f}"
)