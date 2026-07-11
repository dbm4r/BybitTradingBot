from dataclasses import dataclass
from .exchange_balance import ExchangeBalance
@dataclass
class ExchangeSnapshot:

    balance: ExchangeBalance

    positions: list

    orders: list

    trades: list