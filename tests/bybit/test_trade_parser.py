from bybit.parsers.trade_parser import (
    BybitTradeParser,
)
from datetime import datetime

from exchange.exchange_trade import (
    ExchangeTrade,
)


def test_parse_trade():

    item = {
        "execId": "trade-1",
        "orderId": "order-1",
        "symbol": "BTCUSDT",
        "side": "Buy",
        "execQty": "0.25",
        "execPrice": "65000",
        "execFee": "2.15",
        "execTime": "1720000000000",
    }

    trade = BybitTradeParser.parse(
        item
    )

    assert isinstance(
        trade,
        ExchangeTrade,
    )

    assert trade.trade_id == "trade-1"
    assert trade.order_id == "order-1"
    assert trade.symbol == "BTCUSDT"
    assert trade.side == "Buy"
    assert trade.quantity == 0.25
    assert trade.price == 65000.0
    assert trade.fee == 2.15
    expected = datetime.fromtimestamp(
        1720000000000 / 1000
    )

    assert trade.timestamp == expected


def test_parse_trade_list():

    response = {
        "result": {
            "list": [
                {
                    "execId": "1",
                    "orderId": "11",
                    "symbol": "BTCUSDT",
                    "side": "Buy",
                    "execQty": "0.1",
                    "execPrice": "60000",
                    "execFee": "1",
                    "execTime": "1000",
                },
                {
                    "execId": "2",
                    "orderId": "22",
                    "symbol": "ETHUSDT",
                    "side": "Sell",
                    "execQty": "2",
                    "execPrice": "3000",
                    "execFee": "0.5",
                    "execTime": "2000",
                },
            ]
        }
    }

    trades = BybitTradeParser.parse_list(
        response
    )

    assert len(trades) == 2

    assert trades[0].trade_id == "1"
    assert trades[1].trade_id == "2"


def test_parse_empty_trade_list():

    response = {
        "result": {
            "list": []
        }
    }

    trades = BybitTradeParser.parse_list(
        response
    )

    assert trades == []


def test_trade_string():

    trade = ExchangeTrade(
        trade_id="1",
        order_id="2",
        symbol="BTCUSDT",
        side="Buy",
        quantity=0.25,
        price=65000,
        fee=1.2,
        timestamp="1000",
    )

    expected = (
        "BTCUSDT | "
        "Buy | "
        "0.250000 @ "
        "65000.00"
    )

    assert str(trade) == expected