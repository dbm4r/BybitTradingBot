from dataclasses import dataclass
import os

from dotenv import load_dotenv

load_dotenv()


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
    exchange: str = os.getenv("EXCHANGE", "BYBIT")

    # Bybit
    api_key: str = os.getenv("BYBIT_API_KEY", "xdRbOU4VvVZcwxOcEG")
    api_secret: str = os.getenv("BYBIT_API_SECRET", "s798S41QJlK10r3zcyPIWxD7p9Tjo70PNrpa")
    base_url: str = os.getenv(
        "BYBIT_BASE_URL",
        "https://api-demo.bybit.com"
    )

   