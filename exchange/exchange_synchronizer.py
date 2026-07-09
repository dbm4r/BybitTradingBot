class ExchangeSynchronizer:

    def __init__(
        self,
        engine
    ):

        self.engine = engine

    def synchronize(self):

        exchange = self.engine.exchange

        if self.engine.settings.exchange == "PAPER":

            return

        balance = exchange.get_balance()

        print("\n========== ACCOUNT ==========")
        print(balance)
        print("=============================\n")