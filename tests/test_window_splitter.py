import pandas as pd

from validation.window_splitter import (
    WindowSplitter,
)


df = pd.DataFrame(
    {
        "close": range(100)
    }
)

splitter = WindowSplitter()

windows = splitter.split(
    dataframe=df,
    train_size=60,
    test_size=20,
)

print(len(windows))

for index, window in enumerate(windows):

    print(
        index,
        len(window.train),
        len(window.test),
    )