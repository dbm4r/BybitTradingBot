import asyncio
import json
import websockets
import ssl


class MarketSocket:

    URL = "wss://stream.bybit.com/v5/public/linear"

    def __init__(
        self,
        symbol,
        interval,
        on_candle=None
    ):

        self.symbol = symbol
        self.interval = interval
        self.on_candle = on_candle

    async def connect(self):

        async with websockets.connect(
            self.URL,
            ssl=ssl._create_unverified_context()
        ) as websocket:

            print("Connected to Bybit WebSocket")

            await websocket.send(
                json.dumps(
                    {
                        "op": "subscribe",
                        "args": [
                            f"kline.{self.interval}.{self.symbol}"
                        ]
                    }
                )
            )

            print("Subscribed")

            while True:

                message = await websocket.recv()

                data = json.loads(message)

                if "data" not in data:
                    continue

                candle = data["data"][0]

                if not candle["confirm"]:
                    continue

                print(f"Closed candle: {candle['close']}")

                if self.on_candle is not None:
                    await self.on_candle(candle)