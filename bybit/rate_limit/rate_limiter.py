import threading
import time


class RateLimiter:

    def __init__(
        self,
        requests_per_second: float = 10.0,
    ):

        self.requests_per_second = requests_per_second

        self.minimum_interval = (
            1.0 / requests_per_second
        )

        self.last_request = 0.0

        self.lock = threading.Lock()

    def wait(self) -> None:

        with self.lock:

            now = time.perf_counter()

            elapsed = (
                now - self.last_request
            )

            remaining = (
                self.minimum_interval
                - elapsed
            )

            if remaining > 0:

                time.sleep(
                    remaining
                )

            self.last_request = (
                time.perf_counter()
            )