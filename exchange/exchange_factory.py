from exchange.paper_exchange import PaperExchange
from exchange.bybit_exchange import BybitExchange


class ExchangeFactory:

    @staticmethod
    def create(
        name,
        settings=None,
        symbol=None,
    ):

        if name == "PAPER":

            return PaperExchange(
                symbol=symbol,
            )
        if name == "BYBIT":

            return BybitExchange(
                api_key=settings.api_key,
                api_secret=settings.api_secret,
                base_url=settings.base_url,
                symbol=symbol,
            )

        raise ValueError(
            f"Unknown exchange: {name}"
        )