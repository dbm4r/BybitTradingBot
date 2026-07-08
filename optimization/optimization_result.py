from dataclasses import dataclass


@dataclass
class OptimizationResult:

    strategy: str

    parameters: dict

    roi: float

    net_profit: float

    win_rate: float

    trades: int

    max_drawdown: float