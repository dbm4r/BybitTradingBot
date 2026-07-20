from bybit.parsers.candle_parser import CandleParser

from data.mappers.candle_dataframe_mapper import (
    CandleDataFrameMapper,
)


class HistoricalPipeline:

    @staticmethod
    def process(
        response: dict,
        symbol: str,
        interval: str,
    ):

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

        return CandleDataFrameMapper.map(
            candles
        )