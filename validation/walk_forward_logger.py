import pandas as pd


class WalkForwardLogger:

    @staticmethod
    def export(
        results,
        filename,
    ):

        rows = []

        for index, result in enumerate(
            results,
            start=1,
        ):

            rows.append(
                {
                    "Window": index,
                    "Strategy": result.strategy,
                    "Parameters": str(
                        result.parameters
                    ),
                    "Train ROI": result.train_roi,
                    "Test ROI": result.test_roi,
                    "Train Profit": result.train_profit,
                    "Test Profit": result.test_profit,
                    "Train Trades": result.train_trades,
                    "Test Trades": result.test_trades,
                }
            )

        dataframe = pd.DataFrame(rows)

        dataframe.to_csv(
            filename,
            index=False,
        )

        print(
            f"Walk-forward results exported to {filename}"
        )