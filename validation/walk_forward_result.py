from dataclasses import dataclass


@dataclass
class WalkForwardResult:

    strategy: str

    parameters: dict

    train_roi: float

    test_roi: float

    train_profit: float

    test_profit: float

    train_trades: int

    test_trades: int