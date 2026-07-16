from dataclasses import dataclass
from datetime import datetime

from portfolio.portfolio_performance import (
    PortfolioPerformance,
)
from portfolio.portfolio_statistics import (
    PortfolioStatistics,
)


@dataclass(slots=True, frozen=True)
class PortfolioReport:

    timestamp: datetime

    statistics: PortfolioStatistics

    performance: PortfolioPerformance

    @property
    def portfolio_value(self) -> float:

        return self.statistics.portfolio_value

    @property
    def cash(self) -> float:

        return self.statistics.cash

    @property
    def invested_capital(self) -> float:

        return self.statistics.invested_capital

    @property
    def open_positions(self) -> int:

        return self.statistics.open_positions

    @property
    def total_return_percent(self) -> float:

        return self.performance.total_return_percent

    @property
    def capital_utilization_percent(self) -> float:

        return (
            self.performance.capital_utilization_percent
        )

    @property
    def fee_percent(self) -> float:

        return self.performance.fee_percent