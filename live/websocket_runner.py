from bybit.websocket.market_socket import MarketSocket


class WebSocketRunner:

    def __init__(
        self,
        symbol,
        interval
    ):

        self.socket = MarketSocket(
            symbol=symbol,
            interval=interval
        )

    async def run(self):

        await self.socket.connect()