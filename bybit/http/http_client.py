import json

import requests

from bybit.retry.retry_policy import RetryPolicy


class HttpClient:

    def __init__(
        self,
        retry_policy: RetryPolicy | None = None,
        timeout: tuple[int, int] = (5, 30),
    ):

        self.retry_policy = (
            retry_policy
            or RetryPolicy()
        )

        self.timeout = timeout

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
            "timeout": self.timeout,
        }

        if params is not None:
            request_kwargs["params"] = params

        if body is not None:
            request_kwargs["data"] = json.dumps(
                body,
                separators=(",", ":"),
            )

        response = self.retry_policy.execute(
            lambda: requests.request(
                **request_kwargs
            )
        )

        response.raise_for_status()

        return response.json()