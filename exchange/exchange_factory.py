from config import (
    BYBIT_API_KEY,
    BYBIT_API_SECRET,
)

from exchange.bybit_exchange import BybitExchange
from exchange.paper_exchange import PaperExchange


class ExchangeFactory:

    @staticmethod
    def create(
        name: str = "BYBIT",
        settings=None,
        symbol=None,
    ):

        name = name.upper()

        if name == "PAPER":

            return PaperExchange(
                symbol=symbol,
            )

        if name == "BYBIT":

            return BybitExchange(
                api_key=BYBIT_API_KEY,
                api_secret=BYBIT_API_SECRET,
                symbol=symbol,
            )

        raise ValueError(
            f"Unknown exchange: {name}"
        )