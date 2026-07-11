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
        self.engine.portfolio.cash = (
            balance.available_balance
        )
        positions = exchange.get_positions()
        # trades = exchange.get_trade_history()
        orders = exchange.get_open_orders()
        self.engine.order_manager.clear()

        print("\n========== ACCOUNT ==========")
        print(balance)
        print("=============================")
        print(
            f"Portfolio Cash: "
            f"{self.engine.portfolio.cash:.2f}"
        )

        print("\n========= POSITIONS =========")

        if not positions:

            print("No open positions.")

        else:

            for exchange_position in positions:

                position = self.engine.portfolio.get_position(
                    exchange_position.symbol
                )

                position.quantity = (
                    exchange_position.quantity
                )

                position.entry_price = (
                    exchange_position.average_price
                )

                print(exchange_position)

        print("=============================\n")
        print("\n========= OPEN ORDERS =========")

        if not orders:

            print("No open orders.")

        else:

            for order in orders:

                self.engine.order_manager.restore(
                    order
                )

                print(order)

        print("===============================\n")