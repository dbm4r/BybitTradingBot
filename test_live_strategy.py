from bybit.bybit_client import BybitClient
from live.candle_provider import CandleProvider

client = BybitClient(
    api_key="YOUR_KEY",
    api_secret="YOUR_SECRET",
    base_url="https://api-demo.bybit.com"
)

provider = CandleProvider(client)

df = provider.recent_candles(
    symbol="BTCUSDT",
    interval="1",
    limit=200
)

print(df.tail())