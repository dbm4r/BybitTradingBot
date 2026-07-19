from exchange.exchange_symbol import ExchangeSymbol


class BybitSymbolParser:

    @staticmethod
    def parse(
        item: dict,
    ) -> ExchangeSymbol:

        lot_size = item["lotSizeFilter"]
        price_filter = item["priceFilter"]

        return ExchangeSymbol(
            symbol=item["symbol"],
            base_coin=item["baseCoin"],
            quote_coin=item["quoteCoin"],
            status=item["status"],
            tick_size=float(price_filter["tickSize"]),
            qty_step=float(lot_size["qtyStep"]),
            min_order_qty=float(lot_size["minOrderQty"]),
            max_order_qty=float(lot_size["maxOrderQty"]),
            is_tradable=item["status"] == "Trading",
        )

    @classmethod
    def parse_list(
        cls,
        response: dict,
    ) -> list[ExchangeSymbol]:

        return [
            cls.parse(item)
            for item in response["result"]["list"]
        ]