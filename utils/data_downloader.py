import pandas as pd


class DataDownloader:

    @staticmethod
    def save_to_csv(df, filename):
        df.to_csv(filename, index=False)
    def create_dataframe(response):
        candles = response["result"]["list"]

        columns = [
            "timestamp",
            "open",
            "high",
            "low",
            "close",
            "volume",
            "turnover"
        ]

        df = pd.DataFrame(candles, columns=columns)

        # Convert timestamp
        df["timestamp"] = pd.to_datetime(
            df["timestamp"].astype("int64"),
            unit="ms"
        )

        # Convert numeric columns
        numeric_columns = [
            "open",
            "high",
            "low",
            "close",
            "volume",
            "turnover"
        ]

        df[numeric_columns] = df[numeric_columns].astype(float)
        df = df.sort_values("timestamp").reset_index(drop=True)

        return df
    

