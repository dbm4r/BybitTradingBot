from dataclasses import dataclass


@dataclass
class BacktestResult:

    strategy: str

    parameters: dict

    trades: list

    final_balance: float

    roi: float

    net_profit: float

    win_rate: float

    max_drawdown: float