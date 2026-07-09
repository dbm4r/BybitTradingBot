from exchange.exchange import Exchange


class BybitExchange(Exchange):

    def __init__(
        self,
        client
    ):

        self.client = client

    def place_market_order(
        self,
        symbol,
        side,
        quantity
    ):

        pass

    def place_limit_order(
        self,
        symbol,
        side,
        quantity,
        price
    ):

        pass

    def cancel_order(
        self,
        order_id
    ):

        pass

    def get_balance(self):

        pass

    def get_positions(self):

        pass

    def get_open_orders(self):

        pass