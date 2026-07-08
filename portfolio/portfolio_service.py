from portfolio.position_manager import PositionManager

class PortfolioService:

    @staticmethod
    def open_position(
        portfolio,
        position,
        quantity,
        price,
        timestamp,
        cash_after_fee,
        stop_price,
        take_profit_price
    ):
        PositionManager.open(
            position,
            quantity,
            price,
            timestamp
        )

        position_cost = quantity * price


        portfolio.cash = (
            cash_after_fee - position_cost
        )

        position.stop_price = stop_price
        position.take_profit_price = take_profit_price

        position.highest_price = price

        position.break_even_active = False
        position.trailing_active = False
    @staticmethod
    def close_position(
        portfolio,
        position,
        cash_received
    ):

        portfolio.cash = cash_received

        PositionManager.close(position)