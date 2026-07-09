from dataclasses import dataclass


@dataclass
class Settings:

    initial_balance: float = 10000

    trading_fee: float = 0.00055
    slippage_percent: float = 0.0005

    risk_per_trade: float = 0.02

    stop_loss_percent: float = 0.01
    take_profit_percent: float = 0.02

    trailing_stop_percent: float = 0.01
    break_even_trigger_percent: float = 0.01
    trailing_activation_percent: float = 0.02
    exchange: str = "PAPER"
    