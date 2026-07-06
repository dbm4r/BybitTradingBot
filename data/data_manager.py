from api.bybit_api import BybitAPI
from utils.data_downloader import DataDownloader


class DataManager:

    def __init__(self):
        self.api = BybitAPI()

    def _format_interval(self, interval: str) -> str:
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
        return intervals.get(interval, interval)


    def download_historical_data(
        self,
        symbol: str,
        interval: str,
        limit: int = 200
    ):
        response = self.api.get_kline_data(
            symbol=symbol,
            interval=interval,
            limit=limit
        )

        df = DataDownloader.create_dataframe(response)

        formatted_interval = self._format_interval(interval)
        filename = f"data/historical/{symbol}_{formatted_interval}.csv"

        DataDownloader.save_to_csv(df, filename)

        return df
    