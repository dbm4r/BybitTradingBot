import pytest

from bybit.exception_mapper import BybitExceptionMapper

from exceptions.authentication_error import AuthenticationError
from exceptions.insufficient_balance_error import (
    InsufficientBalanceError,
)
from exceptions.order_not_found_error import (
    OrderNotFoundError,
)
from exceptions.rate_limit_error import RateLimitError
from exceptions.server_error import ServerError
from exceptions.unknown_exchange_error import (
    UnknownExchangeError,
)
from exceptions.validation_error import ValidationError


def test_success_response():

    response = {
        "retCode": 0,
        "retMsg": "OK",
        "result": {},
    }

    BybitExceptionMapper.raise_for_response(
        response
    )


def test_authentication_error():

    response = {
        "retCode": 10003,
        "retMsg": "Invalid API key",
    }

    with pytest.raises(
        AuthenticationError
    ) as error:

        BybitExceptionMapper.raise_for_response(
            response
        )

    exception = error.value

    assert exception.code == 10003
    assert exception.exchange == "Bybit"
    assert exception.raw_response == response


def test_validation_error():

    response = {
        "retCode": 10001,
        "retMsg": "Parameter error",
    }

    with pytest.raises(
        ValidationError
    ):

        BybitExceptionMapper.raise_for_response(
            response
        )


def test_insufficient_balance_error():

    response = {
        "retCode": 110004,
        "retMsg": "Insufficient balance",
    }

    with pytest.raises(
        InsufficientBalanceError
    ):

        BybitExceptionMapper.raise_for_response(
            response
        )


def test_order_not_found_error():

    response = {
        "retCode": 1100016,
        "retMsg": "Order not found",
    }

    with pytest.raises(
        OrderNotFoundError
    ):

        BybitExceptionMapper.raise_for_response(
            response
        )


def test_rate_limit_error():

    response = {
        "retCode": 10006,
        "retMsg": "Too many requests",
    }

    with pytest.raises(
        RateLimitError
    ):

        BybitExceptionMapper.raise_for_response(
            response
        )


def test_server_error():

    response = {
        "retCode": 10016,
        "retMsg": "Internal server error",
    }

    with pytest.raises(
        ServerError
    ):

        BybitExceptionMapper.raise_for_response(
            response
        )


def test_unknown_error():

    response = {
        "retCode": 999999,
        "retMsg": "Unknown",
    }

    with pytest.raises(
        UnknownExchangeError
    ) as error:

        BybitExceptionMapper.raise_for_response(
            response
        )

    exception = error.value

    assert exception.code == 999999
    assert exception.exchange == "Bybit"


def test_default_message():

    response = {
        "retCode": 999999,
    }

    with pytest.raises(
        UnknownExchangeError
    ) as error:

        BybitExceptionMapper.raise_for_response(
            response
        )

    assert (
        error.value.message
        == "Unknown exchange error."
    )


def test_exchange_error_string():

    response = {
        "retCode": 10003,
        "retMsg": "Invalid API key",
    }

    with pytest.raises(
        AuthenticationError
    ) as error:

        BybitExceptionMapper.raise_for_response(
            response
        )

    assert (
        str(error.value)
        == "[Bybit:10003] Invalid API key"
    )