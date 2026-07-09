from dataclasses import dataclass


@dataclass
class Config:

    symbol: str = "BTCUSDT"

    interval: str = "60"

    limit: int = 500

    strategy: str = "SMA"

    mode: str = "optimization"
    # mode: str = "single"
    # mode: str = "comparison"
    exchange: str = "PAPER"