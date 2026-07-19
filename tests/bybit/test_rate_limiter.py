import time

from bybit.rate_limit.rate_limiter import RateLimiter


def test_default_configuration():

    limiter = RateLimiter()

    assert limiter.requests_per_second == 10.0
    assert limiter.minimum_interval == 0.1


def test_custom_configuration():

    limiter = RateLimiter(
        requests_per_second=5,
    )

    assert limiter.requests_per_second == 5
    assert limiter.minimum_interval == 0.2


def test_wait_does_not_fail():

    limiter = RateLimiter()

    limiter.wait()


def test_wait_respects_rate_limit():

    limiter = RateLimiter(
        requests_per_second=5,
    )

    start = time.perf_counter()

    limiter.wait()
    limiter.wait()

    elapsed = time.perf_counter() - start

    assert elapsed >= 0.19


def test_multiple_waits():

    limiter = RateLimiter(
        requests_per_second=20,
    )

    start = time.perf_counter()

    for _ in range(5):

        limiter.wait()

    elapsed = time.perf_counter() - start

    assert elapsed >= 0.20