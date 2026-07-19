from exceptions.exchange_error import ExchangeError


class InsufficientBalanceError(ExchangeError):
    """
    Account has insufficient balance.
    """