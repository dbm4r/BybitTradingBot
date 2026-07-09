from exchange.paper_exchange import PaperExchange


class ExchangeFactory:

    @staticmethod
    def create(name: str):

        exchanges = {

            "PAPER": PaperExchange,

        }

        if name not in exchanges:

            raise ValueError(
                f"Unknown exchange: {name}"
            )

        return exchanges[name]()