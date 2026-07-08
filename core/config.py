from dataclasses import dataclass, field


@dataclass
class Config:

    symbol: str = "BTCUSDT"

    interval: str = "60"

    limit: int = 500

    strategy: str = "SMA"

    strategy_parameters: dict = field(
        default_factory=lambda: {
            "fast_period": 20,
            "slow_period": 50
        }
    )