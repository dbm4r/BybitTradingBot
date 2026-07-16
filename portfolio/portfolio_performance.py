from dataclasses import dataclass

from portfolio.portfolio_statistics import (
    PortfolioStatistics,
)


@dataclass(slots=True, frozen=True)
class PortfolioPerformance:

    total_return_percent: float

    capital_utilization_percent: float

    fee_percent: float

    @classmethod
    def from_statistics(
        cls,
        initial_balance: float,
        statistics: PortfolioStatistics,
    ):

        total_return = (
            (
                statistics.portfolio_value
                - initial_balance
            )
            / initial_balance
        ) * 100

        utilization = 0.0

        if statistics.portfolio_value > 0:

            utilization = (
                statistics.invested_capital
                / statistics.portfolio_value
            ) * 100

        fee_percent = (
            statistics.total_fees
            / initial_balance
        ) * 100

        return cls(
            total_return_percent=total_return,
            capital_utilization_percent=utilization,
            fee_percent=fee_percent,
        )