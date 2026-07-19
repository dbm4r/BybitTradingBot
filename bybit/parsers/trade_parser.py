from datetime import datetime

from exchange.exchange_trade import ExchangeTrade


class BybitTradeParser:

    @staticmethod
    def parse(
        item: dict,
    ) -> ExchangeTrade:

        return ExchangeTrade(
            trade_id=item["execId"],
            order_id=item["orderId"],
            symbol=item["symbol"],
            side=item["side"],
            quantity=float(item["execQty"]),
            price=float(item["execPrice"]),
            fee=float(item["execFee"]),
            timestamp=datetime.fromtimestamp(
                int(item["execTime"]) / 1000
            ),
        )

    @classmethod
    def parse_list(
        cls,
        response: dict,
    ) -> list[ExchangeTrade]:

        return [
            cls.parse(item)
            for item in response["result"]["list"]
        ]