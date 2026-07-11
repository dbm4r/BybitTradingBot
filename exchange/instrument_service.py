from exchange.instrument import Instrument


class InstrumentService:

    def __init__(self, client):

        self.client = client

    def get(
        self,
        symbol
    ):

        response = self.client.market.get_instruments(
            symbol=symbol
        )

        item = response["result"]["list"][0]

        return Instrument(
            symbol=item["symbol"],
            qty_step=float(
                item["lotSizeFilter"]["qtyStep"]
            ),
            min_qty=float(
                item["lotSizeFilter"]["minOrderQty"]
            ),
            max_qty=float(
                item["lotSizeFilter"]["maxOrderQty"]
            ),
            tick_size=float(
                item["priceFilter"]["tickSize"]
            )
        )