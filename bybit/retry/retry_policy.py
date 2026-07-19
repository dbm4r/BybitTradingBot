import time

import requests


class RetryPolicy:

    RETRYABLE_STATUS_CODES = {
        429,
        500,
        502,
        503,
        504,
    }

    MAX_RETRIES = 3

    BACKOFF_SECONDS = 1.0

    @classmethod
    def execute(
        cls,
        operation,
    ):

        last_exception = None

        for attempt in range(
            cls.MAX_RETRIES + 1
        ):

            try:

                response = operation()

                if (
                    response.status_code
                    in cls.RETRYABLE_STATUS_CODES
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

                if attempt == cls.MAX_RETRIES:
                    raise

                time.sleep(
                    cls.BACKOFF_SECONDS
                    * (2 ** attempt)
                )

        raise last_exception