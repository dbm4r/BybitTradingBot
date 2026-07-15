from market.timeframe import Timeframe
from market.timeframe_utils import TimeframeUtils


print("========== TIMEFRAME UTILS ==========\n")

for timeframe in Timeframe:

    print(
        f"{timeframe.name:<4} -> "
        f"{TimeframeUtils.minutes(timeframe)} minutes"
    )