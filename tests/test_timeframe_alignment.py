from datetime import datetime

from market.timeframe import Timeframe
from market.timeframe_alignment import TimeframeAlignment


tests = [
    (datetime(2026, 7, 15, 13, 41, 27), Timeframe.M5),
    (datetime(2026, 7, 15, 13, 44, 58), Timeframe.M5),
    (datetime(2026, 7, 15, 13, 45, 3), Timeframe.M5),
    (datetime(2026, 7, 15, 13, 59, 10), Timeframe.H1),
    (datetime(2026, 7, 15, 15, 27, 12), Timeframe.H4),
    (datetime(2026, 7, 15, 18, 43, 1), Timeframe.D1),
]

print("========== TIMEFRAME ALIGNMENT ==========\n")

for timestamp, timeframe in tests:

    aligned = TimeframeAlignment.align(
        timestamp,
        timeframe,
    )

    print(
        f"{timestamp} -> {timeframe.name:<3} -> {aligned}"
    )