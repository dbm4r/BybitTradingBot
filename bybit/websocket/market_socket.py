import asyncio
import json
import websockets


class MarketSocket:

    URL = "wss://stream-demo.bybit.com/v5/public/linear"

    async def connect(self):

        async with websockets.connect(
            self.URL
        ) as websocket:

            print("Connected to Bybit WebSocket")

            await websocket.send(
                json.dumps(
                    {
                        "op": "subscribe",
                        "args": [
                            "kline.1.BTCUSDT"
                        ]
                    }
                )
            )

            print("Subscribed")

            while True:

                message = await websocket.recv()

                print(message)