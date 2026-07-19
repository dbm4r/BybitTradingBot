import json

import requests

from bybit.rate_limit.rate_limiter import RateLimiter
from bybit.retry.retry_policy import RetryPolicy
from bybit.timeout.timeout_policy import TimeoutPolicy


class HttpClient:

    def __init__(
        self,
        retry_policy: RetryPolicy | None = None,
        timeout_policy: TimeoutPolicy | None = None,
        rate_limiter: RateLimiter | None = None,
    ):

        self.retry_policy = (
            retry_policy
            or RetryPolicy()
        )

        self.timeout_policy = (
            timeout_policy
            or TimeoutPolicy()
        )

        self.rate_limiter = (
            rate_limiter
            or RateLimiter()
        )

    def send(
        self,
        method: str,
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
        body: dict | None = None,
    ):

        request_kwargs = {
            "method": method,
            "url": url,
            "headers": headers,
            "timeout": self.timeout_policy.timeout,
        }

        if params is not None:
            request_kwargs["params"] = params

        if body is not None:
            request_kwargs["data"] = json.dumps(
                body,
                separators=(",", ":"),
            )

        self.rate_limiter.wait()

        response = self.retry_policy.execute(
            lambda: requests.request(
                **request_kwargs,
            )
        )

        response.raise_for_status()

        return response.json()