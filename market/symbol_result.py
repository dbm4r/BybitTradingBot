from dataclasses import dataclass


@dataclass
class SymbolResult:

    symbol: str

    roi: float

    net_profit: float

    trades: int

    max_drawdown: float