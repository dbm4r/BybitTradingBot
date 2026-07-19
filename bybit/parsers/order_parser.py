from datetime import datetime

from exchange.exchange_order import ExchangeOrder


class BybitOrderParser:

    @staticmethod
    def parse_create_order(
        response: dict,
        symbol: str,
        side: str,
        quantity: float,
    ) -> ExchangeOrder:

        result = response["result"]

        return ExchangeOrder(
            order_id=result["orderId"],
            client_order_id=result.get("orderLinkId"),
            symbol=symbol,
            side=side,
            quantity=quantity,
            filled_quantity=0,
            remaining_quantity=quantity,
            status="NEW",
            average_price=None,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            raw_response=response,
        )

    @staticmethod
    def parse_open_order(
        item: dict,
    ) -> ExchangeOrder:

        quantity = float(item["qty"])
        filled = float(item.get("cumExecQty", 0))

        return ExchangeOrder(
            order_id=item["orderId"],
            client_order_id=item.get("orderLinkId"),
            symbol=item["symbol"],
            side=item["side"],
            quantity=quantity,
            filled_quantity=filled,
            remaining_quantity=quantity - filled,
            status=item["orderStatus"],
            average_price=(
                float(item["avgPrice"])
                if item.get("avgPrice")
                else None
            ),
            created_at=None,
            updated_at=None,
            raw_response=item,
        )

    @classmethod
    def parse_open_orders(
        cls,
        response: dict,
    ) -> list[ExchangeOrder]:

        return [
            cls.parse_open_order(item)
            for item in response["result"]["list"]
        ]

    @classmethod
    def parse_order(
        cls,
        response: dict,
    ) -> ExchangeOrder:

        return cls.parse_open_order(
            response["result"]["list"][0]
        )