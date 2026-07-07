import pandas as pd


class RiskMetrics:

    @staticmethod
    def calculate_drawdown(equity_curve: pd.DataFrame):

        df = equity_curve.copy()

        df["Peak"] = df["Portfolio Value"].cummax()

        df["Drawdown"] = (
            df["Portfolio Value"] - df["Peak"]
        ) / df["Peak"] * 100

        return df

    @staticmethod
    def max_drawdown(equity_curve: pd.DataFrame):

        df = RiskMetrics.calculate_drawdown(equity_curve)

        return df["Drawdown"].min()