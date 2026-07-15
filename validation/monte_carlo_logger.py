import pandas as pd


class MonteCarloLogger:

    @staticmethod
    def export(
        results,
        filename,
    ):

        rows = []

        for result in results:

            rows.append(
                {
                    "Iteration": result.iteration,
                    "ROI": result.roi,
                    "Net Profit": result.net_profit,
                    "Max Drawdown": result.max_drawdown,
                    "Trades": result.trades,
                }
            )

        dataframe = pd.DataFrame(rows)

        dataframe.to_csv(
            filename,
            index=False,
        )

        print(
            f"Monte Carlo results exported to {filename}"
        )