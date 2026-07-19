from exceptions.exchange_error import ExchangeError


class RateLimitError(ExchangeError):
    """
    Exchange rate limit exceeded.
    """