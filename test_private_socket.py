import asyncio

from core.settings import Settings
from bybit.websocket.private_socket import PrivateSocket


settings = Settings()

socket = PrivateSocket(
    api_key=settings.api_key,
    api_secret=settings.api_secret
)

asyncio.run(
    socket.connect()
)