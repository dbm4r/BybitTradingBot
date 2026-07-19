from datetime import datetime

from bybit.parsers.order_parser import (
    BybitOrderParser,
)

from exchange.exchange_order import (
    ExchangeOrder,
)


def test_parse_create_order():

    response = {
        "result": {
            "orderId": "12345",
            "orderLinkId": "client-1",
        }
    }

    order = BybitOrderParser.parse_create_order(
        response=response,
        symbol="BTCUSDT",
        side="Buy",
        quantity=0.5,
    )

    assert isinstance(
        order,
        ExchangeOrder,
    )

    assert order.order_id == "12345"
    assert order.client_order_id == "client-1"
    assert order.symbol == "BTCUSDT"
    assert order.side == "Buy"
    assert order.quantity == 0.5
    assert order.filled_quantity == 0
    assert order.remaining_quantity == 0.5
    assert order.status == "NEW"
    assert order.average_price is None

    assert isinstance(
        order.created_at,
        datetime,
    )

    assert isinstance(
        order.updated_at,
        datetime,
    )

    assert order.raw_response == response


def test_parse_open_order():

    item = {
        "orderId": "12345",
        "orderLinkId": "client-1",
        "symbol": "BTCUSDT",
        "side": "Sell",
        "qty": "2",
        "cumExecQty": "0.5",
        "orderStatus": "PartiallyFilled",
        "avgPrice": "65000",
    }

    order = BybitOrderParser.parse_open_order(
        item
    )

    assert order.order_id == "12345"
    assert order.client_order_id == "client-1"
    assert order.symbol == "BTCUSDT"
    assert order.side == "Sell"
    assert order.quantity == 2.0
    assert order.filled_quantity == 0.5
    assert order.remaining_quantity == 1.5
    assert order.status == "PartiallyFilled"
    assert order.average_price == 65000.0
    assert order.raw_response == item


def test_parse_open_order_without_average_price():

    item = {
        "orderId": "12345",
        "symbol": "BTCUSDT",
        "side": "Buy",
        "qty": "1",
        "cumExecQty": "0",
        "orderStatus": "New",
        "avgPrice": "",
    }

    order = BybitOrderParser.parse_open_order(
        item
    )

    assert order.average_price is None


def test_parse_open_orders():

    response = {
        "result": {
            "list": [
                {
                    "orderId": "1",
                    "symbol": "BTCUSDT",
                    "side": "Buy",
                    "qty": "1",
                    "cumExecQty": "0",
                    "orderStatus": "New",
                    "avgPrice": "",
                },
                {
                    "orderId": "2",
                    "symbol": "ETHUSDT",
                    "side": "Sell",
                    "qty": "3",
                    "cumExecQty": "1",
                    "orderStatus": "PartiallyFilled",
                    "avgPrice": "3000",
                },
            ]
        }
    }

    orders = BybitOrderParser.parse_open_orders(
        response
    )

    assert len(orders) == 2

    assert orders[0].order_id == "1"

    assert orders[1].order_id == "2"


def test_parse_empty_open_orders():

    response = {
        "result": {
            "list": []
        }
    }

    orders = BybitOrderParser.parse_open_orders(
        response
    )

    assert orders == []


def test_parse_order():

    response = {
        "result": {
            "list": [
                {
                    "orderId": "999",
                    "symbol": "BTCUSDT",
                    "side": "Buy",
                    "qty": "0.25",
                    "cumExecQty": "0.10",
                    "orderStatus": "PartiallyFilled",
                    "avgPrice": "64000",
                }
            ]
        }
    }

    order = BybitOrderParser.parse_order(
        response
    )

    assert order.order_id == "999"
    assert order.symbol == "BTCUSDT"
    assert order.quantity == 0.25
    assert order.filled_quantity == 0.10
    assert order.remaining_quantity == 0.15
    assert order.average_price == 64000.0