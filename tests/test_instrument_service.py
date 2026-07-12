from core.settings import Settings
from bybit.bybit_client import BybitClient
from exchange.instrument_service import InstrumentService

settings = Settings()

client = BybitClient(
    api_key=settings.api_key,
    api_secret=settings.api_secret,
    base_url=settings.base_url
)

service = InstrumentService(client)

instrument = service.get("BTCUSDT")

print(instrument)

quantity = 0.15542884689696865

rounded = instrument.round_quantity(quantity)

print(f"Original : {quantity}")
print(f"Rounded  : {rounded}")

