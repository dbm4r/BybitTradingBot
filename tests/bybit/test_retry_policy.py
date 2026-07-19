from unittest.mock import Mock

import pytest
import requests

from bybit.retry.retry_policy import RetryPolicy


def test_success_first_attempt():

    policy = RetryPolicy()

    response = Mock()
    response.status_code = 200

    operation = Mock(
        return_value=response
    )

    result = policy.execute(
        operation
    )

    assert result is response

    assert operation.call_count == 1


def test_retry_connection_error_then_success():

    policy = RetryPolicy()

    response = Mock()
    response.status_code = 200

    operation = Mock(
        side_effect=[
            requests.ConnectionError(),
            response,
        ]
    )

    result = policy.execute(
        operation
    )

    assert result is response

    assert operation.call_count == 2


def test_retry_timeout_then_success():

    policy = RetryPolicy()

    response = Mock()
    response.status_code = 200

    operation = Mock(
        side_effect=[
            requests.Timeout(),
            response,
        ]
    )

    result = policy.execute(
        operation
    )

    assert result is response

    assert operation.call_count == 2


def test_retry_http_error_then_success():

    policy = RetryPolicy()

    bad = Mock()
    bad.status_code = 503

    good = Mock()
    good.status_code = 200

    operation = Mock(
        side_effect=[
            bad,
            good,
        ]
    )

    result = policy.execute(
        operation
    )

    assert result is good

    assert operation.call_count == 2


def test_max_retries_exceeded():

    policy = RetryPolicy(
        max_retries=2,
    )

    operation = Mock(
        side_effect=requests.ConnectionError()
    )

    with pytest.raises(
        requests.ConnectionError
    ):

        policy.execute(
            operation
        )

    assert operation.call_count == 3


def test_non_retryable_status_code():

    policy = RetryPolicy()

    response = Mock()
    response.status_code = 404

    operation = Mock(
        return_value=response
    )

    result = policy.execute(
        operation
    )

    assert result is response

    assert operation.call_count == 1