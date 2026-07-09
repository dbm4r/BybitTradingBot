from dataclasses import dataclass


@dataclass
class Settings:

    # Portfolio
    initial_balance: float = 10000

    # Costs
    trading_fee: float = 0.00055
    slippage_percent: float = 0.0005

    # Risk
    risk_per_trade: float = 0.02
    stop_loss_percent: float = 0.01
    take_profit_percent: float = 0.02

    trailing_stop_percent: float = 0.01
    break_even_trigger_percent: float = 0.01
    trailing_activation_percent: float = 0.02

    # Exchange
    exchange: str = "PAPER"

    # API
    # api_key: str = ""
    # api_secret: str = ""

    # Environment
    # base_url: str = ""