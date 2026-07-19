from exceptions.exchange_error import ExchangeError


class ValidationError(ExchangeError):
    """
    Invalid request parameters.
    """