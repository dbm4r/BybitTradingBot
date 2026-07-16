from dataclasses import dataclass

from backtesting.portfolio import Portfolio


@dataclass(slots=True, frozen=True)
class PortfolioStatistics:

    cash: float

    invested_capital: float

    portfolio_value: float

    open_positions: int

    realized_pnl: float

    unrealized_pnl: float

    total_pnl: float

    total_fees: float

    @classmethod
    def from_portfolio(
        cls,
        portfolio: Portfolio,
        total_fees: float = 0.0,
        unrealized_pnl: float = 0.0,
        realized_pnl: float = 0.0,
    ):

        invested = 0.0

        open_positions = 0

        for position in portfolio.positions.values():

            if not position.is_open():
                continue

            open_positions += 1

            invested += (
                position.quantity
                * position.average_price
            )

        total_pnl = (
            realized_pnl
            + unrealized_pnl
        )

        portfolio_value = (
            portfolio.cash
            + invested
            + unrealized_pnl
        )

        return cls(
            cash=portfolio.cash,
            invested_capital=invested,
            portfolio_value=portfolio_value,
            open_positions=open_positions,
            realized_pnl=realized_pnl,
            unrealized_pnl=unrealized_pnl,
            total_pnl=total_pnl,
            total_fees=total_fees,
        )