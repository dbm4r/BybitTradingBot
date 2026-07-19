from dataclasses import dataclass


@dataclass(slots=True)
class ExchangeOperation:

    success: bool

    message: str | None = None

    raw_response: dict | None = None