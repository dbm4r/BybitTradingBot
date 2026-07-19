from bybit.parsers.instrument_parser import (
    BybitInstrumentParser,
)


def test_parse_instrument():

    item = {
        "symbol": "BTCUSDT",
        "lotSizeFilter": {
            "qtyStep": "0.001",
            "minOrderQty": "0.001",
            "maxOrderQty": "100"
        },
        "priceFilter": {
            "tickSize": "0.10"
        }
    }

    instrument = BybitInstrumentParser.parse(
        item
    )

    assert instrument.symbol == "BTCUSDT"

    assert instrument.qty_step == 0.001

    assert instrument.min_qty == 0.001

    assert instrument.max_qty == 100.0

    assert instrument.tick_size == 0.10