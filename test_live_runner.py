from bybit.bybit_client import BybitClient
from live.live_runner import LiveRunner
from strategies.ema_crossover import EMACrossoverStrategy


client = BybitClient(
    api_key="xdRbOU4VvVZcwxOcEG",
    api_secret="s798S41QJlK10r3zcyPIWxD7p9Tjo70PNrpa",
    base_url="https://api-demo.bybit.com"
)

strategy = EMACrossoverStrategy(
    fast_period=20,
    slow_period=50
)

runner = LiveRunner(
    client=client,
    strategy=strategy,
    execution_engine=None,
    symbol="BTCUSDT",
    interval=1
)

runner.run()