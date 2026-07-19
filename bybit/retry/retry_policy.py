import time

import requests


class RetryPolicy:

    def __init__(
        self,
        max_retries: int = 3,
        initial_delay: float = 1.0,
        multiplier: float = 2.0,
        retryable_status_codes: set[int] | None = None,
    ):

        self.max_retries = max_retries
        self.initial_delay = initial_delay
        self.multiplier = multiplier

        self.retryable_status_codes = (
            retryable_status_codes
            or {
                429,
                500,
                502,
                503,
                504,
            }
        )

    def execute(
        self,
        operation,
    ):

        delay = self.initial_delay

        last_exception = None

        for attempt in range(
            self.max_retries + 1
        ):

            try:

                response = operation()

                if (
                    response.status_code
                    in self.retryable_status_codes
                ):
                    raise requests.HTTPError(
                        response=response
                    )

                return response

            except (
                requests.ConnectionError,
                requests.Timeout,
                requests.HTTPError,
            ) as exception:

                last_exception = exception

                if attempt >= self.max_retries:
                    raise

                time.sleep(delay)

                delay *= self.multiplier

        raise last_exception