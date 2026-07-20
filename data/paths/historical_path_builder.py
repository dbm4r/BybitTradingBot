from pathlib import Path


class HistoricalPathBuilder:

    _INTERVALS = {
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

    @classmethod
    def build(
        cls,
        symbol: str,
        interval: str,
    ) -> str:

        interval_name = cls._INTERVALS.get(
            interval,
            interval,
        )

        path = (
            Path("data")
            / "historical"
            / f"{symbol}_{interval_name}.csv"
        )

        return str(path)