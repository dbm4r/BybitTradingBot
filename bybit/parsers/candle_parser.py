from datetime import datetime

from models.candle import Candle


class CandleParser:

    @staticmethod
    def parse(
        symbol: str,
        interval: str,
        item: list,
    ) -> Candle:

        return Candle(
            symbol=symbol,
            interval=interval,
            timestamp=datetime.fromtimestamp(
                int(item[0]) / 1000
            ),
            open=float(item[1]),
            high=float(item[2]),
            low=float(item[3]),
            close=float(item[4]),
            volume=float(item[5]),
            turnover=float(item[6]),
        )