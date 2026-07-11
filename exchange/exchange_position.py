from dataclasses import dataclass


@dataclass
class ExchangePosition:

    symbol: str
    side: str
    quantity: float
    average_price: float
    unrealized_pnl: float

    def __str__(self):

        return (
            f"{self.symbol} | "
            f"{self.side} | "
            f"Qty: {self.quantity:.6f} | "
            f"Avg: {self.average_price:.2f} | "
            f"PnL: {self.unrealized_pnl:.2f}"
        )