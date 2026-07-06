from pybit.unified_trading import HTTP
from config import (
    BYBIT_API_KEY,
    BYBIT_API_SECRET,
    BYBIT_TESTNET
)


class BybitAPI:
    def __init__(self):
        self.session = HTTP(
            testnet=BYBIT_TESTNET,
            api_key=BYBIT_API_KEY,
            api_secret=BYBIT_API_SECRET,
        )

    def get_server_time(self):
        return self.session.get_server_time()
    
    def get_kline_data(self, symbol: str, interval: str, limit: int = 200):
        return self.session.get_kline(
        category="linear",
        symbol=symbol,
        interval=interval,
        limit=limit,
        )