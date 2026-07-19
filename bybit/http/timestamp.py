import time


class Timestamp:

    @staticmethod
    def now() -> str:

        return str(
            int(time.time() * 1000)
        )