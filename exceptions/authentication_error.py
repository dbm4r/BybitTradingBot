from exceptions.exchange_error import ExchangeError


class AuthenticationError(ExchangeError):
    """
    Invalid API credentials or signature.
    """