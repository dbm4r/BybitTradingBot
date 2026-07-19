import json

import requests

from bybit.retry.retry_policy import RetryPolicy


class HttpClient:

    def send(
        self,
        method: str,
        url: str,
        headers=None,
        params=None,
        body=None,
        timeout=(5, 30),
    ):

        request_kwargs = {
            "method": method,
            "url": url,
            "headers": headers,
            "timeout": timeout,
        }

        if params is not None:
            request_kwargs["params"] = params

        if body is not None:

            request_kwargs["data"] = json.dumps(
                body,
                separators=(",", ":"),
            )

        response = RetryPolicy.execute(
            lambda: requests.request(
                **request_kwargs,
            )
        )

        response.raise_for_status()

        return response.json()