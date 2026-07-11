import asyncio
import json
import ssl

import websockets

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

            while True:

                message = await websocket.recv()

                print(message)