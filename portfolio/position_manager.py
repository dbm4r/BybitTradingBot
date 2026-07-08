from portfolio.position_direction import PositionDirection
class PositionManager:

    @staticmethod
    def open(
        position,
        quantity,
        entry_price,
        entry_time,
        stop_price,
        take_profit_price
    ):

        position.quantity = quantity

        position.entry_price = entry_price
        position.entry_time = entry_time

        position.stop_price = stop_price
        position.take_profit_price = take_profit_price

        position.highest_price = entry_price

        position.break_even_active = False
        position.trailing_active = False

    @staticmethod
    def close(position):

        position.close()
        position.direction = PositionDirection.LONG
    @staticmethod
    def add(
        position,
        quantity,
        price
    ):

        position.entry_price = (
            position.average_entry_price(
                quantity,
                price
            )
        )

        position.quantity += quantity

        if position.highest_price is None:

            position.highest_price = price

        else:

            position.highest_price = max(
                position.highest_price,
                price
            )
    @staticmethod
    def move_stop(
        position,
        stop_price
    ):

        position.stop_price = stop_price
    @staticmethod
    def move_take_profit(
        position,
        take_profit_price
    ):

        position.take_profit_price = take_profit_price
    @staticmethod
    def reduce(
        position,
        quantity
    ):

        position.quantity -= quantity

        if position.quantity <= 0:

            PositionManager.close(position)