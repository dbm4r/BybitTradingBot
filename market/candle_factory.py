from models.candle import Candle


class CandleFactory:

    @staticmethod
    def from_series(
        row,
        symbol: str,
        interval: str,
    ) -> Candle:

        return Candle.from_series(
            row=row,
            symbol=symbol,
            interval=interval,
        )

    @staticmethod
    def from_dict(
        data: dict,
        symbol: str,
        interval: str,
    ) -> Candle:

        return Candle.from_dict(
            symbol=symbol,
            interval=interval,
            data=data,
        )

    @staticmethod
    def from_bybit(
        data: dict,
        symbol: str,
        interval: str,
    ) -> Candle:

        return Candle.from_bybit(
            symbol=symbol,
            interval=interval,
            data=data,
        )