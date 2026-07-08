class PortfolioService:

    @staticmethod
    def open_position(
        portfolio,
        quantity,
        price,
        timestamp,
        cash_after_fee,
        stop_price,
        take_profit_price
    ):

        position_cost = quantity * price

        portfolio.position = quantity

        portfolio.cash = (
            cash_after_fee - position_cost
        )

        portfolio.entry_price = price
        portfolio.entry_time = timestamp

        portfolio.stop_price = stop_price
        portfolio.take_profit_price = take_profit_price

        portfolio.highest_price = price

        portfolio.break_even_active = False
        portfolio.trailing_active = False
    @staticmethod
    def close_position(
        portfolio,
        cash_received
    ):

        portfolio.cash = cash_received

        portfolio.position = 0

        portfolio.entry_price = None
        portfolio.entry_time = None

        portfolio.stop_price = None
        portfolio.take_profit_price = None

        portfolio.highest_price = None

        portfolio.break_even_active = False
        portfolio.trailing_active = False