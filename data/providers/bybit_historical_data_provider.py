from exchange.exchange import Exchange

from data.models.historical_data_request import (
    HistoricalDataRequest,
)
from data.providers.historical_data_provider import (
    HistoricalDataProvider,
)


class BybitHistoricalDataProvider(
    HistoricalDataProvider,
):

    def __init__(
        self,
        exchange: Exchange,
    ):

        self.exchange = exchange

    def download(
        self,
        request: HistoricalDataRequest,
    ):

        return self.exchange.get_candles(
            symbol=request.symbol,
            interval=request.interval,
            start=int(
                request.start.timestamp() * 1000
            ),
            end=int(
                request.end.timestamp() * 1000
            ),
            limit=request.limit,
        )