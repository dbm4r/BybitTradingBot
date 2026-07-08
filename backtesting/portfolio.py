from portfolio.position import Position

class Portfolio:

    def __init__(self, initial_balance: float):

        self.initial_balance = initial_balance

        self.cash = initial_balance
        self.positions = {}

        self.position = 0.0

        self.entry_price = None
        self.entry_time = None
        self.stop_price = None
        self.take_profit_price = None
        self.highest_price = None
        self.break_even_active = False
        self.trailing_active = False

    def get_position(self, symbol):

        if symbol not in self.positions:

            self.positions[symbol] = Position(symbol)

        return self.positions[symbol]
    
    def has_position(self, symbol):

        return self.get_position(symbol).quantity > 0

    def in_position(self):

        return self.position > 0

    def market_value(self, current_price: float):

        return self.position * current_price

    def total_value(self, current_price: float):

        return self.cash + self.market_value(current_price)