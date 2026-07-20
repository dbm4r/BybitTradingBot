from datetime import UTC
from datetime import datetime

import pandas as pd

from data.validation.time_gap_detector import (
    TimeGapDetector,
)


def dataframe(*timestamps):

    return pd.DataFrame(
        {
            "timestamp": list(
                timestamps,
            )
        }
    )


def test_no_gaps():

    detector = TimeGapDetector()

    report = detector.detect(
        dataframe(
            datetime(
                2024,
                1,
                1,
                0,
                0,
                tzinfo=UTC,
            ),
            datetime(
                2024,
                1,
                1,
                0,
                1,
                tzinfo=UTC,
            ),
            datetime(
                2024,
                1,
                1,
                0,
                2,
                tzinfo=UTC,
            ),
        ),
        "1",
    )

    assert report.has_gaps is False

    assert report.total_missing_candles == 0

    assert len(report.gaps) == 0


def test_single_gap():

    detector = TimeGapDetector()

    report = detector.detect(
        dataframe(
            datetime(
                2024,
                1,
                1,
                0,
                0,
                tzinfo=UTC,
            ),
            datetime(
                2024,
                1,
                1,
                0,
                2,
                tzinfo=UTC,
            ),
        ),
        "1",
    )

    assert report.has_gaps

    assert report.total_missing_candles == 1

    assert len(report.gaps) == 1

    gap = report.gaps[0]

    assert gap.missing_candles == 1

    assert gap.start == datetime(
        2024,
        1,
        1,
        0,
        1,
        tzinfo=UTC,
    )

    assert gap.end == datetime(
        2024,
        1,
        1,
        0,
        1,
        tzinfo=UTC,
    )


def test_multiple_gaps():

    detector = TimeGapDetector()

    report = detector.detect(
        dataframe(
            datetime(
                2024,
                1,
                1,
                0,
                0,
                tzinfo=UTC,
            ),
            datetime(
                2024,
                1,
                1,
                0,
                3,
                tzinfo=UTC,
            ),
            datetime(
                2024,
                1,
                1,
                0,
                6,
                tzinfo=UTC,
            ),
        ),
        "1",
    )

    assert report.has_gaps

    assert report.total_missing_candles == 4

    assert len(report.gaps) == 2


def test_empty_dataframe():

    detector = TimeGapDetector()

    report = detector.detect(
        pd.DataFrame(
            {
                "timestamp": [],
            }
        ),
        "1",
    )

    assert report.has_gaps is False

    assert report.total_missing_candles == 0


def test_invalid_interval():

    detector = TimeGapDetector()

    import pytest

    with pytest.raises(
        ValueError,
    ):

        detector.detect(
            dataframe(
                datetime.now(
                    UTC,
                )
            ),
            "XYZ",
        )