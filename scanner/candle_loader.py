from models.candle import Candle
from models.candle_series import CandleSeries
from bybit.parsers.candle_parser import CandleParser

class CandleLoader:

    @staticmethod
    def load(
        response,
        symbol: str,
        interval: str,
    ) -> CandleSeries:

        series = CandleSeries(
            symbol=symbol,
            interval=interval,
        )

        for item in reversed(response["result"]["list"]):

            series.add(
                CandleParser.parse(
                    symbol=symbol,
                    interval=interval,
                    item=item,
                )
            )

        return series