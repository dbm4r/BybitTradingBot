from exchange.exchange import Exchange


class PaperExchange(Exchange):

    def place_market_order(
        self,
        symbol,
        side,
        quantity
    ):

        print(
            f"[PAPER] MARKET {side} "
            f"{quantity:.6f} {symbol}"
        )

        return {
            "symbol": symbol,
            "side": side,
            "quantity": quantity,
            "status": "FILLED"
        }

    def place_limit_order(
        self,
        symbol,
        side,
        quantity,
        price
    ):

        print(
            f"[PAPER] LIMIT {side} "
            f"{quantity:.6f} {symbol}"
            f" @ {price:.2f}"
        )

    def cancel_order(
        self,
        order_id
    ):

        print(
            f"[PAPER] Cancel {order_id}"
        )

    def get_balance(self):

        return 0

    def get_positions(self):

        return []

    def get_open_orders(self):

        return []