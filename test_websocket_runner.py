import asyncio

from live.websocket_runner import WebSocketRunner


async def candle_received(candle):

    print()

    print("========== CLOSED CANDLE ==========")
    print(candle)
    print("===================================\n")


runner = WebSocketRunner(
    symbol="BTCUSDT",
    interval="1"
)

runner.socket.on_candle = candle_received

asyncio.run(
    runner.run()
)