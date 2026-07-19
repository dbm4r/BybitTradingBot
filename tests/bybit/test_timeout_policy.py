from bybit.timeout.timeout_policy import (
    TimeoutPolicy,
)


def test_default_timeout():

    policy = TimeoutPolicy()

    assert policy.connect_timeout == 5
    assert policy.read_timeout == 30
    assert policy.timeout == (5, 30)


def test_custom_timeout():

    policy = TimeoutPolicy(
        connect_timeout=2,
        read_timeout=10,
    )

    assert policy.connect_timeout == 2
    assert policy.read_timeout == 10
    assert policy.timeout == (2, 10)


def test_timeout_property():

    policy = TimeoutPolicy(
        connect_timeout=8,
        read_timeout=60,
    )

    timeout = policy.timeout

    assert isinstance(
        timeout,
        tuple,
    )

    assert len(timeout) == 2

    assert timeout == (8, 60)