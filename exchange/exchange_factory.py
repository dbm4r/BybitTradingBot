from exchange.paper_exchange import PaperExchange
from bybit.bybit_client import BybitClient
from bybit.bybit_exchange import BybitExchange


class ExchangeFactory:

    @staticmethod
    def create(
        name,
        settings=None
    ):

        if name == "PAPER":

            return PaperExchange()

        if name == "BYBIT":

            client = BybitClient(
                api_key="",
                api_secret="",
                base_url=""
            )

            return BybitExchange(client)

        raise ValueError(
            f"Unknown exchange: {name}"
        )