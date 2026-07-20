import pandas as pd

from data.synchronization.dataframe_merge_service import (
    DataFrameMergeService,
)


def create_dataframe(rows):

    return pd.DataFrame(
        rows
    )


def test_merge_removes_duplicates_and_sorts():

    existing = create_dataframe(
        [
            {
                "timestamp": 1,
                "close": 100,
            },
            {
                "timestamp": 3,
                "close": 300,
            },
        ]
    )

    incoming = create_dataframe(
        [
            {
                "timestamp": 2,
                "close": 200,
            },
            {
                "timestamp": 3,
                "close": 350,
            },
        ]
    )

    service = DataFrameMergeService()

    result = service.merge(
        existing=existing,
        incoming=incoming,
    )

    assert list(
        result["timestamp"]
    ) == [
        1,
        2,
        3,
    ]

    assert len(result) == 3

    assert result.iloc[-1]["close"] == 350


def test_merge_empty_existing():

    existing = pd.DataFrame()

    incoming = create_dataframe(
        [
            {
                "timestamp": 1,
                "close": 100,
            }
        ]
    )

    service = DataFrameMergeService()

    result = service.merge(
        existing=existing,
        incoming=incoming,
    )

    assert len(result) == 1