from exchange.exchange import Exchange
from bybit.parsers.candle_parser import CandleParser
from utils.data_downloader import DataDownloader


class DataManager:

    def __init__(
        self,
        exchange: Exchange,
    ):

        self.exchange = exchange

    @staticmethod
    def _format_interval(
        interval: str,
    ) -> str:

        intervals = {
            "1": "1m",
            "3": "3m",
            "5": "5m",
            "15": "15m",
            "30": "30m",
            "60": "1h",
            "120": "2h",
            "240": "4h",
            "360": "6h",
            "720": "12h",
            "D": "1d",
            "W": "1w",
            "M": "1M",
        }

        return intervals.get(
            interval,
            interval,
        )

    def download_historical_data(
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

        candles = []

        for item in reversed(
            response["result"]["list"]
        ):

            candles.append(
                CandleParser.parse(
                    symbol=symbol,
                    interval=interval,
                    item=item,
                )
            )

        df = DataDownloader.from_candles(
            candles
        )

        filename = (
            f"data/historical/"
            f"{symbol}_{self._format_interval(interval)}.csv"
        )

        DataDownloader.save_to_csv(
            df,
            filename,
        )

        return df