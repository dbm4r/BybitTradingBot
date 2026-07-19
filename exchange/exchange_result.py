from dataclasses import dataclass

from exchange.exchange_order import ExchangeOrder


@dataclass(slots=True)
class ExchangeResult:

    success: bool

    order: ExchangeOrder | None = None

    error: str | None = None

    raw_response: dict | None = None