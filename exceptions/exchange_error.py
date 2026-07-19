from typing import Any


class ExchangeError(Exception):

    def __init__(
        self,
        message: str,
        code: int | None = None,
        exchange: str | None = None,
        raw_response: dict[str, Any] | None = None,
    ):

        super().__init__(message)

        self.message = message
        self.code = code
        self.exchange = exchange
        self.raw_response = raw_response

    def __str__(self):

        parts = []

        if self.exchange:
            parts.append(self.exchange)

        if self.code is not None:
            parts.append(str(self.code))

        prefix = ""

        if parts:
            prefix = "[" + ":".join(parts) + "] "

        return prefix + self.message