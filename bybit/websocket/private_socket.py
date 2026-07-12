import asyncio
import json
import ssl

import websockets
from live.private_dispatcher import PrivateDispatcher
from bybit.websocket.auth import WebSocketAuth


class PrivateSocket:

    URL = "wss://stream-demo.bybit.com/v5/private"

    def __init__(
        self,
        api_key,
        api_secret
    ):

        self.auth = WebSocketAuth(
            api_key,
            api_secret
        )
        self.dispatcher = PrivateDispatcher()

    async def connect(self):

        async with websockets.connect(
            self.URL,
            ssl=ssl._create_unverified_context()
        ) as websocket:

            print("Connected")

            await websocket.send(
                json.dumps(
                    self.auth.generate()
                )
            )

            print("Auth request sent")

            response = json.loads(
                await websocket.recv()
            )

            print(response)

            if not response.get("success"):
                raise RuntimeError(
                    "Authentication failed"
                )

            await websocket.send(
                json.dumps(
                    {
                        "op": "subscribe",
                        "args": [
                            "order",
                            "execution",
                            "position",
                            "wallet"
                        ]
                    }
                )
            )

            print("Subscribed to private topics")

            while True:

                message = await websocket.recv()

                data = json.loads(message)

                if "topic" not in data:
                    continue

                self.dispatcher.dispatch(data)