from pprint import pprint

from bybit.bybit_client import BybitClient


client = BybitClient(
    api_key="xdRbOU4VvVZcwxOcEG",
    api_secret="s798S41QJlK10r3zcyPIWxD7p9Tjo70PNrpa",
    base_url = "https://api-demo.bybit.com"
)

print("=" * 60)
print("SERVER TIME")
print("=" * 60)
pprint(
    client.market.get_server_time()
)

print("\n" + "=" * 60)
print("WALLET BALANCE")
print("=" * 60)
pprint(
    client.account.get_wallet_balance()
)

print("\n" + "=" * 60)
print("BTCUSDT TICKER")
print("=" * 60)
pprint(
    client.market.get_tickers(
        symbol="BTCUSDT"
    )
)

print("\n" + "=" * 60)
print("BTCUSDT INSTRUMENT")
print("=" * 60)
pprint(
    client.market.get_instruments(
        symbol="BTCUSDT"
    )
)

print("\n" + "=" * 60)
print("BTCUSDT KLINES")
print("=" * 60)
pprint(
    client.market.get_kline(
        symbol="BTCUSDT",
        interval="60",
        limit=2
    )
)
print("\n" + "=" * 60)
print("MARKET ORDER")
print("=" * 60)

pprint(
    client.trade.place_market_order(
        symbol="BTCUSDT",
        side="Buy",
        quantity=0.001
    )
)

print("\n" + "=" * 60)
print("POSITIONS")
print("=" * 60)

pprint(
    client.trade.get_positions(
        symbol="BTCUSDT"
    )
)

print("\n" + "=" * 60)
print("CLOSE POSITION")
print("=" * 60)

pprint(
    client.trade.close_position(
        symbol="BTCUSDT"
    )
)

print("\n" + "=" * 60)
print("POSITIONS AFTER CLOSE")
print("=" * 60)

pprint(
    client.trade.get_positions(
        symbol="BTCUSDT"
    )
)
print("\n" + "=" * 60)
print("LIMIT ORDER")
print("=" * 60)

response = client.trade.place_limit_order(
    symbol="BTCUSDT",
    side="Buy",
    quantity=0.001,
    price=50000
)

pprint(response)
print("\n" + "=" * 60)
print("OPEN ORDERS")
print("=" * 60)

orders = client.trade.get_open_orders(
    symbol="BTCUSDT"
)

pprint(orders)
print("\n" + "=" * 60)
print("CANCEL ORDER")
print("=" * 60)

order_id = response["result"]["orderId"]

pprint(
    client.trade.cancel_order(
        symbol="BTCUSDT",
        order_id=order_id
    )
)
print("\n" + "=" * 60)
print("OPEN ORDERS AFTER CANCEL")
print("=" * 60)

pprint(
    client.trade.get_open_orders(
        symbol="BTCUSDT"
    )
)
print("\n" + "=" * 60)
print("OPEN ORDERS AFTER CANCEL")
print("=" * 60)

pprint(
    client.trade.get_open_orders(
        symbol="BTCUSDT"
    )
)

print("\n" + "=" * 60)
print("CLEAN ALL OPEN ORDERS")
print("=" * 60)

orders = client.trade.get_open_orders(
    symbol="BTCUSDT"
)

for order in orders["result"]["list"]:

    print(f"Cancelling {order['orderId']}")

    pprint(
        client.trade.cancel_order(
            symbol="BTCUSDT",
            order_id=order["orderId"]
        )
    )

print("\n" + "=" * 60)
print("OPEN ORDERS AFTER CLEANUP")
print("=" * 60)

pprint(
    client.trade.get_open_orders(
        symbol="BTCUSDT"
    )
)
print("\n" + "=" * 60)
print("GET ORDER")
print("=" * 60)

response = client.trade.place_limit_order(
    symbol="BTCUSDT",
    side="Buy",
    quantity=0.001,
    price=50000
)

order_id = response["result"]["orderId"]

pprint(
    client.trade.get_order(
        order_id=order_id
    )
)