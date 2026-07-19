from exceptions.exchange_error import ExchangeError


class ServerError(ExchangeError):
    """
    Exchange internal server error.
    """