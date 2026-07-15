from datetime import datetime

from market.timeframe import Timeframe
from market.timeframe_utils import TimeframeUtils


class TimeframeAlignment:

    @staticmethod
    def align(
        timestamp: datetime,
        timeframe: Timeframe,
    ) -> datetime:

        minutes = TimeframeUtils.minutes(timeframe)

        if minutes < 60:

            aligned_minute = (
                timestamp.minute // minutes
            ) * minutes

            return timestamp.replace(
                minute=aligned_minute,
                second=0,
                microsecond=0,
            )

        if timeframe == Timeframe.H1:

            return timestamp.replace(
                minute=0,
                second=0,
                microsecond=0,
            )

        if timeframe == Timeframe.H4:

            aligned_hour = (
                timestamp.hour // 4
            ) * 4

            return timestamp.replace(
                hour=aligned_hour,
                minute=0,
                second=0,
                microsecond=0,
            )

        if timeframe == Timeframe.D1:

            return timestamp.replace(
                hour=0,
                minute=0,
                second=0,
                microsecond=0,
            )

        raise ValueError(
            f"Unsupported timeframe: {timeframe}"
        )