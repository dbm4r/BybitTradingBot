from bybit.bybit_client import BybitClient


client = BybitClient(
    api_key="",
    api_secret="",
    base_url="https://api-testnet.bybit.com"
)

response = client.get_server_time()

print(response)