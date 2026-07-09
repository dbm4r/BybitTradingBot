from dataclasses import dataclass

from exchange.exchange_order import ExchangeOrder


@dataclass
class ExchangeResult:

    success: bool

    order: ExchangeOrder | None = None

    error: str | None = None