import pandas as pd


class EquityCurve:

    def __init__(self):

        self.timestamps = []

        self.values = []

    def add(self, timestamp, value):

        self.timestamps.append(timestamp)

        self.values.append(value)

    def dataframe(self):

        return pd.DataFrame({

            "Timestamp": self.timestamps,

            "Portfolio Value": self.values

        })