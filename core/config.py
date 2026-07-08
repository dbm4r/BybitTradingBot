from dataclasses import dataclass


@dataclass
class Config:

    symbol: str = "BTCUSDT"

    interval: str = "60"

    limit: int = 500

    strategy: str = "SMA"