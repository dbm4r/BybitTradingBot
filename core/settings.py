from dataclasses import dataclass


@dataclass
class Settings:

    initial_balance: float = 10000

    trading_fee: float = 0.00055

    slippage: float = 0.0

    risk_per_trade: float = 0.02
    
    stop_loss_percent: float = 0.01