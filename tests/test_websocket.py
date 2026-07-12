import asyncio

from bybit.websocket.market_socket import MarketSocket


socket = MarketSocket()

asyncio.run(
    socket.connect()
)