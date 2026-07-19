from exceptions.exchange_error import ExchangeError


class NetworkError(ExchangeError):
    """
    Network or connection failure.
    """