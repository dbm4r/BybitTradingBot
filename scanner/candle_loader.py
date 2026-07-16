from models.candle import Candle
from models.candle_series import CandleSeries


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

        for item in reversed(
            response["result"]["list"]
        ):

            candle = Candle(
                symbol=symbol,
                interval=interval,
                timestamp=item[0],
                open=float(item[1]),
                high=float(item[2]),
                low=float(item[3]),
                close=float(item[4]),
                volume=float(item[5]),
                turnover=float(item[6]),
            )

            series.add(
                candle
            )

        return series