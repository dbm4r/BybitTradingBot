class PrivateDispatcher:

    def dispatch(
        self,
        event
    ):

        topic = event.get("topic")

        if topic == "order":
            self.handle_order(event)

        elif topic == "execution":
            self.handle_execution(event)

        elif topic == "position":
            self.handle_position(event)

        elif topic == "wallet":
            self.handle_wallet(event)

    def handle_order(
        self,
        event
    ):

        order = event["data"][0]

        print("\n========== ORDER ==========")
        print(f"Symbol : {order['symbol']}")
        print(f"Side   : {order['side']}")
        print(f"Status : {order['orderStatus']}")
        print(f"Qty    : {order['qty']}")
        print(f"Price  : {order['avgPrice']}")
        print("===========================\n")

    def handle_execution(
        self,
        event
    ):

        execution = event["data"][0]

        print("\n======== EXECUTION ========")
        print(f"Symbol : {execution['symbol']}")
        print(f"Side   : {execution['side']}")
        print(f"Qty    : {execution['execQty']}")
        print(f"Price  : {execution['execPrice']}")
        print(f"Fee    : {execution['execFee']}")
        print("===========================\n")

    def handle_position(
        self,
        event
    ):

        position = event["data"][0]

        print("\n========= POSITION =========")
        print(f"Symbol : {position['symbol']}")
        print(f"Side   : {position['side']}")
        print(f"Size   : {position['size']}")
        print(f"Entry  : {position['entryPrice']}")
        print(f"PnL    : {position['unrealisedPnl']}")
        print("============================\n")

    def handle_wallet(
        self,
        event
    ):

        wallet = event["data"][0]

        print("\n========== WALLET ==========")
        print(f"Equity    : {wallet['totalEquity']}")
        print(f"Available : {wallet['totalAvailableBalance']}")
        print("============================\n")