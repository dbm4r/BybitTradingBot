from exceptions.exchange_error import ExchangeError


class OrderNotFoundError(ExchangeError):
    """
    Order could not be found.
    """