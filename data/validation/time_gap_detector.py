from datetime import timedelta

import pandas as pd

from data.validation.gap_detector import (
    GapDetector,
)
from data.validation.gap_report import (
    GapReport,
)
from data.validation.missing_range import (
    MissingRange,
)


class TimeGapDetector(
    GapDetector,
):

    def detect(
        self,
        dataframe: pd.DataFrame,
        interval: str,
    ) -> GapReport:

        if dataframe.empty:

            return GapReport(
                has_gaps=False,
                gaps=[],
                total_missing_candles=0,
            )

        timestamps = dataframe["timestamp"].sort_values()

        expected = self._interval(
            interval,
        )

        gaps = []

        previous = timestamps.iloc[0]

        for current in timestamps.iloc[1:]:

            difference = current - previous

            if difference > expected:

                missing = (
                    int(
                        difference / expected
                    ) - 1
                )

                gaps.append(
                    MissingRange(
                        start=previous + expected,
                        end=current - expected,
                        missing_candles=missing,
                    )
                )

            previous = current

        return GapReport(
            has_gaps=len(gaps) > 0,
            gaps=gaps,
            total_missing_candles=sum(
                gap.missing_candles
                for gap in gaps
            ),
        )

    @staticmethod
    def _interval(
        interval: str,
    ) -> timedelta:

        mapping = {
            "1": timedelta(minutes=1),
            "3": timedelta(minutes=3),
            "5": timedelta(minutes=5),
            "15": timedelta(minutes=15),
            "30": timedelta(minutes=30),
            "60": timedelta(hours=1),
            "120": timedelta(hours=2),
            "240": timedelta(hours=4),
            "360": timedelta(hours=6),
            "720": timedelta(hours=12),
            "D": timedelta(days=1),
            "W": timedelta(weeks=1),
        }

        if interval not in mapping:

            raise ValueError(
                f"Unsupported interval: {interval}"
            )

        return mapping[interval]