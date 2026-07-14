from datetime import datetime

from models.candle import Candle
from models.candle_series import CandleSeries


def test_add_candles():

    series = CandleSeries(
        symbol="BTCUSDT",
        interval="1",
    )

    series.add(
        Candle(
            symbol="BTCUSDT",
            interval="1",
            timestamp=datetime.now(),
            open=100,
            high=105,
            low=95,
            close=103,
            volume=120,
            turnover=12360,
        )
    )

    series.add(
        Candle(
            symbol="BTCUSDT",
            interval="1",
            timestamp=datetime.now(),
            open=103,
            high=110,
            low=101,
            close=108,
            volume=140,
            turnover=15120,
        )
    )

    assert series.count == 2
    assert series.first.close == 103
    assert series.last.close == 108
    assert series.close_prices == [103, 108]
    assert series.high_prices == [105, 110]