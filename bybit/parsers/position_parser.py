from exchange.exchange_position import ExchangePosition


class BybitPositionParser:

    @staticmethod
    def parse(
        item: dict,
    ) -> ExchangePosition:

        return ExchangePosition(
            symbol=item["symbol"],
            side=item["side"],
            quantity=float(item["size"]),
            average_price=float(item["avgPrice"]),
            unrealized_pnl=float(item["unrealisedPnl"]),
        )

    @classmethod
    def parse_list(
        cls,
        response: dict,
    ) -> list[ExchangePosition]:

        positions = []

        for item in response["result"]["list"]:

            if float(item["size"]) == 0:
                continue

            positions.append(
                cls.parse(item)
            )

        return positions