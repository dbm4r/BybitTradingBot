import pandas as pd


class IndicatorPipeline:

    def __init__(self):

        self._indicators = []

    def add(
        self,
        indicator
    ):

        self._indicators.append(indicator)

        return self

    def calculate(
        self,
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:

        for indicator in self._indicators:

            dataframe = indicator.calculate(dataframe)

        return dataframe