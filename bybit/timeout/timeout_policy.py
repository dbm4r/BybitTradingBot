class TimeoutPolicy:

    def __init__(
        self,
        connect_timeout: int = 5,
        read_timeout: int = 30,
    ):

        self.connect_timeout = connect_timeout
        self.read_timeout = read_timeout

    @property
    def timeout(
        self,
    ) -> tuple[int, int]:

        return (
            self.connect_timeout,
            self.read_timeout,
        )