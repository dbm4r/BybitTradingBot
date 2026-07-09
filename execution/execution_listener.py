class ExecutionListener:

    def __init__(self, engine):

        self.engine = engine

    def poll(self):

        exchange = self.engine.exchange

        if self.engine.settings.exchange == "BYBIT":
            return

        positions = exchange.get_positions()

        open_orders = exchange.get_open_orders()

        return {
            "positions": positions,
            "orders": open_orders
        }