from dataclasses import dataclass


@dataclass
class MonteCarloResult:

    iteration: int

    roi: float

    net_profit: float

    max_drawdown: float

    trades: int