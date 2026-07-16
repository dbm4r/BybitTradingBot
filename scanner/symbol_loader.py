from exchange.exchange_symbol import ExchangeSymbol


class SymbolLoader:

    @staticmethod
    def load(
        response,
    ) -> list[ExchangeSymbol]:

        symbols = []

        items = response["result"]["list"]

        for item in items:

            symbol = ExchangeSymbol(
                symbol=item["symbol"],
                base_coin=item["baseCoin"],
                quote_coin=item["quoteCoin"],
                status=item["status"],
                tick_size=float(
                    item["priceFilter"]["tickSize"]
                ),
                qty_step=float(
                    item["lotSizeFilter"]["qtyStep"]
                ),
                min_order_qty=float(
                    item["lotSizeFilter"]["minOrderQty"]
                ),
                max_order_qty=float(
                    item["lotSizeFilter"]["maxOrderQty"]
                ),
                is_tradable=(
                    item["status"] == "Trading"
                ),
            )

            symbols.append(symbol)

        return symbols