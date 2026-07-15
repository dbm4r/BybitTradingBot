from validation.window import Window


class WindowSplitter:

    def split(
        self,
        dataframe,
        train_size,
        test_size,
    ):

        windows = []

        start = 0

        while True:

            train_end = start + train_size
            test_end = train_end + test_size

            if test_end > len(dataframe):
                break

            train = dataframe.iloc[
                start:train_end
            ].copy()

            test = dataframe.iloc[
                train_end:test_end
            ].copy()

            windows.append(
                Window(
                    train=train,
                    test=test,
                )
            )

            start += test_size

        return windows