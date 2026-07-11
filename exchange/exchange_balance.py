from dataclasses import dataclass


@dataclass
class ExchangeBalance:

    total_equity: float
    wallet_balance: float
    available_balance: float

    def __str__(self):

        return (
            f"Total Equity      : {self.total_equity:.2f}\n"
            f"Wallet Balance    : {self.wallet_balance:.2f}\n"
            f"Available Balance : {self.available_balance:.2f}"
        )