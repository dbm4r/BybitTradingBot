class Portfolio:

    def __init__(self, initial_balance: float):

        self.initial_balance = initial_balance

        self.cash = initial_balance

        self.position = 0.0

        self.entry_price = None
        self.entry_time = None
        self.stop_price = None

    def in_position(self):

        return self.position > 0

    def market_value(self, current_price: float):

        return self.position * current_price

    def total_value(self, current_price: float):

        return self.cash + self.market_value(current_price)