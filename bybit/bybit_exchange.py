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

        raise NotImplementedError

    def place_limit_order(
        self,
        symbol,
        side,
        quantity,
        price
    ):

        raise NotImplementedError

    def cancel_order(
        self,
        order_id
    ):

        raise NotImplementedError

    def get_balance(self):

        raise NotImplementedError

    def get_positions(self):

        raise NotImplementedError

    def get_open_orders(self):

        raise NotImplementedError