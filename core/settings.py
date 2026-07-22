from dataclasses import dataclass
import os

from dotenv import load_dotenv

load_dotenv()
from data.cache.cache_type import (
    CacheType,
)
from data.storage.storage_type import (
    StorageType,
)
load_dotenv()
@dataclass
class Settings:

    # ==========================================
    # Portfolio
    # ==========================================

    initial_balance: float = 10000

    # ==========================================
    # Costs
    # ==========================================

    trading_fee: float = 0.00055
    slippage_percent: float = 0.0005

    # ==========================================
    # Risk
    # ==========================================

    risk_per_trade: float = 0.02
    stop_loss_percent: float = 0.01
    take_profit_percent: float = 0.02

    trailing_stop_percent: float = 0.01
    break_even_trigger_percent: float = 0.01
    trailing_activation_percent: float = 0.02

    # ==========================================
    # Runtime
    # ==========================================

    max_open_positions: int = 10
    max_orders_per_symbol: int = 5

    request_timeout: tuple[int, int] = (5, 30)
    requests_per_second: float = 10.0

    # ==========================================
    # Legacy compatibility
    # ==========================================

    exchange: str = "BYBIT"

    api_key: str = os.getenv(
        "BYBIT_API_KEY",
        "",
    )

    api_secret: str = os.getenv(
        "BYBIT_API_SECRET",
        "",
    )

    base_url: str = os.getenv(
        "BYBIT_BASE_URL",
        "",
    )
    storage_type: StorageType = (
        StorageType.CSV
    )
    cache_type: CacheType = (
        CacheType.MEMORY
    )

    cache_size: int = 10