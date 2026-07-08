class PositionManager:

    @staticmethod
    def open(
        position,
        quantity,
        entry_price,
        entry_time
    ):

        position.quantity = quantity

        position.entry_price = entry_price

        position.entry_time = entry_time

    @staticmethod
    def close(position):

        position.close()
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