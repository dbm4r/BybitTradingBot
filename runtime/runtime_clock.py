from datetime import datetime


class RuntimeClock:

    @staticmethod
    def now() -> datetime:

        return datetime.now()