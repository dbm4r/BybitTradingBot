from datetime import datetime

from portfolio.portfolio_manager import PortfolioManager
from portfolio.portfolio_statistics import (
    PortfolioStatistics,
)
from portfolio.portfolio_performance import (
    PortfolioPerformance,
)
from portfolio.portfolio_report import (
    PortfolioReport,
)
from portfolio.portfolio_formatter import (
    PortfolioFormatter,
)
from strategies.trend.sma_crossover import (
    SMACrossoverStrategy,
)

print(
    "========== PORTFOLIO INTEGRATION ==========\n"
)

manager = PortfolioManager()

strategy = SMACrossoverStrategy()

manager.register_asset(
    symbol="BTCUSDT",
    strategy=strategy,
)

manager.register_asset(
    symbol="ETHUSDT",
    strategy=strategy,
)

manager.register_asset(
    symbol="SOLUSDT",
    strategy=strategy,
)

print("Registered Assets")

for symbol in manager.symbols:

    print(symbol)

print()

statistics = PortfolioStatistics.from_portfolio(
    portfolio=manager.portfolio,
    total_fees=0,
)

performance = PortfolioPerformance.from_statistics(
    initial_balance=manager.portfolio.initial_balance,
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