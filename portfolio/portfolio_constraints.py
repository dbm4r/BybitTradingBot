from dataclasses import dataclass


@dataclass(slots=True)
class PortfolioConstraints:

    max_open_positions: int = 3

    max_portfolio_exposure: float = 1.0

    max_symbol_allocation: float = 0.25