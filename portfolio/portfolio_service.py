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
            position=position,
            quantity=quantity,
            entry_price=price,
            entry_time=timestamp,
            stop_price=stop_price,
            take_profit_price=take_profit_price
        )

        position_cost = quantity * price

        portfolio.cash = (
            cash_after_fee - position_cost
        )
    @staticmethod
    def close_position(
        portfolio,
        position,
        cash_received
    ):

        portfolio.cash = cash_received

        PositionManager.close(position)