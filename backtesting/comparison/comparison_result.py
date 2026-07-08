from dataclasses import dataclass


@dataclass
class ComparisonResult:

    strategy: str

    net_profit: float

    win_rate: float

    trades: int

    max_drawdown: float

    roi: float