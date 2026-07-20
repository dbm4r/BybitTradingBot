import pandas as pd

from data.pipeline.historical_pipeline import (
    HistoricalPipeline,
)


def create_response(*candles):

    return {
        "result": {
            "list": list(candles),
        }
    }


def test_pipeline_process():

    response = create_response(
        [
            "1704067200000",
            "100",
            "110",
            "90",
            "105",
            "50",
            "5000",
        ],
        [
            "1704067260000",
            "105",
            "115",
            "100",
            "110",
            "60",
            "6000",
        ],
    )

    result = HistoricalPipeline.process(
        response=response,
        symbol="BTCUSDT",
        interval="1",
    )

    assert isinstance(
        result,
        pd.DataFrame,
    )

    assert len(result) == 2

    assert "timestamp" in result.columns

    assert "open" in result.columns

    assert "high" in result.columns

    assert "low" in result.columns

    assert "close" in result.columns

    assert "volume" in result.columns


def test_pipeline_order():

    response = create_response(
        [
            "1704067260000",
            "105",
            "115",
            "100",
            "110",
            "60",
            "6000",
        ],
        [
            "1704067200000",
            "100",
            "110",
            "90",
            "105",
            "50",
            "5000",
        ],
    )

    result = HistoricalPipeline.process(
        response=response,
        symbol="BTCUSDT",
        interval="1",
    )

    assert result.iloc[0]["close"] == 105

    assert result.iloc[1]["close"] == 110