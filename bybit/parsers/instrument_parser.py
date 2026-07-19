from exchange.instrument import Instrument


class BybitInstrumentParser:

    @staticmethod
    def parse(
        item: dict,
    ) -> Instrument:

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
            ),
        )