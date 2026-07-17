from exchange.exchange import Exchange
from scanner.candle_loader import CandleLoader
from market.market_data_service import MarketDataService


class MarketDataLoader:

    def __init__(
        self,
        exchange: Exchange,
        service: MarketDataService,
    ):

        self.exchange = exchange
        self.service = service

    def load(
        self,
        symbol: str,
        interval: str,
        limit: int = 200,
    ):

        response = self.exchange.get_candles(
            symbol=symbol,
            interval=interval,
            limit=limit,
        )

        candles = CandleLoader.load(
            response=response,
            symbol=symbol,
            interval=interval,
        )

        series = self.service.create_series(
            symbol=symbol,
            interval=interval,
            max_size=candles.max_size,
        )

        series.clear()

        for candle in candles:

            series.add(
                candle
            )

        return series