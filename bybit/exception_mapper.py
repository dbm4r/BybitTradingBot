from exceptions.authentication_error import AuthenticationError
from exceptions.insufficient_balance_error import (
    InsufficientBalanceError,
)
from exceptions.network_error import NetworkError
from exceptions.order_not_found_error import (
    OrderNotFoundError,
)
from exceptions.rate_limit_error import RateLimitError
from exceptions.server_error import ServerError
from exceptions.unknown_exchange_error import (
    UnknownExchangeError,
)
from exceptions.validation_error import ValidationError


class BybitExceptionMapper:

    _ERROR_MAP = {

        # Authentication

        10003: AuthenticationError,
        10004: AuthenticationError,
        10005: AuthenticationError,
        10007: AuthenticationError,

        # Validation

        10001: ValidationError,
        110001: ValidationError,
        110003: ValidationError,

        # Balance

        110004: InsufficientBalanceError,
        110007: InsufficientBalanceError,
        110012: InsufficientBalanceError,

        # Orders

        1100016: OrderNotFoundError,

        # Rate limits

        10006: RateLimitError,

        # Server

        10016: ServerError,
        10017: ServerError,
    }

    @classmethod
    def raise_for_response(
        cls,
        response: dict,
    ) -> None:

        code = response.get(
            "retCode",
            -1,
        )

        if code == 0:
            return

        message = response.get(
            "retMsg",
            "Unknown exchange error.",
        )

        exception = cls._ERROR_MAP.get(
            code,
            UnknownExchangeError,
        )

        raise exception(
            message=message,
            code=code,
            exchange="Bybit",
            raw_response=response,
        )