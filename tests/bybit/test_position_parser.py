from bybit.parsers.position_parser import (
    BybitPositionParser,
)

from exchange.exchange_position import (
    ExchangePosition,
)


def test_parse_position():

    item = {
        "symbol": "BTCUSDT",
        "side": "Buy",
        "size": "0.250",
        "avgPrice": "65000",
        "unrealisedPnl": "123.45",
    }

    position = BybitPositionParser.parse(
        item
    )

    assert isinstance(
        position,
        ExchangePosition,
    )

    assert position.symbol == "BTCUSDT"
    assert position.side == "Buy"
    assert position.quantity == 0.25
    assert position.average_price == 65000.0
    assert position.unrealized_pnl == 123.45


def test_parse_position_list():

    response = {
        "result": {
            "list": [
                {
                    "symbol": "BTCUSDT",
                    "side": "Buy",
                    "size": "0.5",
                    "avgPrice": "65000",
                    "unrealisedPnl": "100",
                },
                {
                    "symbol": "ETHUSDT",
                    "side": "Sell",
                    "size": "2",
                    "avgPrice": "3000",
                    "unrealisedPnl": "-50",
                },
            ]
        }
    }

    positions = BybitPositionParser.parse_list(
        response
    )

    assert len(positions) == 2

    assert positions[0].symbol == "BTCUSDT"
    assert positions[1].symbol == "ETHUSDT"


def test_zero_size_position_is_ignored():

    response = {
        "result": {
            "list": [
                {
                    "symbol": "BTCUSDT",
                    "side": "Buy",
                    "size": "0",
                    "avgPrice": "65000",
                    "unrealisedPnl": "0",
                }
            ]
        }
    }

    positions = BybitPositionParser.parse_list(
        response
    )

    assert positions == []


def test_empty_position_list():

    response = {
        "result": {
            "list": []
        }
    }

    positions = BybitPositionParser.parse_list(
        response
    )

    assert positions == []


def test_position_string():

    position = ExchangePosition(
        symbol="BTCUSDT",
        side="Buy",
        quantity=0.25,
        average_price=65000,
        unrealized_pnl=123.45,
    )

    expected = (
        "BTCUSDT | "
        "Buy | "
        "Qty: 0.250000 | "
        "Avg: 65000.00 | "
        "PnL: 123.45"
    )

    assert str(position) == expected