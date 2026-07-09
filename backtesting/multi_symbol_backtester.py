class MultiSymbolBacktester:

    def __init__(
        self,
        settings,
        strategy
    ):

        self.settings = settings
        self.strategy = strategy

        self.results = []