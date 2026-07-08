from portfolio.position import Position

class Portfolio:

    def __init__(self, initial_balance: float):

        self.initial_balance = initial_balance

        self.cash = initial_balance
        self.positions = {}


    def get_position(self, symbol):

        if symbol not in self.positions:

            self.positions[symbol] = Position(symbol)

        return self.positions[symbol]
    
    def has_position(self, symbol):

        return self.get_position(symbol).quantity > 0

    def in_position(self, symbol):

        return self.get_position(symbol).is_open()

    def market_value(self, symbol, current_price):

        position = self.get_position(symbol)

        return position.quantity * current_price

    def total_value(
        self,
        symbol,
        current_price
    ):

        return (
            self.cash
            + self.market_value(symbol, current_price)
        )