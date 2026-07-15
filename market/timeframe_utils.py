from market.timeframe import Timeframe


class TimeframeUtils:

    _minutes = {
        Timeframe.M1: 1,
        Timeframe.M3: 3,
        Timeframe.M5: 5,
        Timeframe.M15: 15,
        Timeframe.M30: 30,
        Timeframe.H1: 60,
        Timeframe.H4: 240,
        Timeframe.D1: 1440,
    }

    @classmethod
    def minutes(
        cls,
        timeframe: Timeframe,
    ) -> int:

        return cls._minutes[timeframe]