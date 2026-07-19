from bybit.parsers.symbol_parser import BybitSymbolParser


def test_parse_symbol():

    item = {
        "symbol": "BTCUSDT",
        "baseCoin": "BTC",
        "quoteCoin": "USDT",
        "status": "Trading",
        "lotSizeFilter": {
            "minOrderQty": "0.001",
            "maxOrderQty": "100",
            "qtyStep": "0.001",
        },
        "priceFilter": {
            "tickSize": "0.10",
        },
    }

    symbol = BybitSymbolParser.parse(
        item
    )

    assert symbol.symbol == "BTCUSDT"

    assert symbol.base_coin == "BTC"

    assert symbol.quote_coin == "USDT"

    assert symbol.status == "Trading"

    assert symbol.tick_size == 0.10

    assert symbol.qty_step == 0.001

    assert symbol.min_order_qty == 0.001

    assert symbol.max_order_qty == 100.0

    assert symbol.is_tradable is True