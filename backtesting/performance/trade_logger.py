import pandas as pd


class TradeLogger:

    @staticmethod
    def export(trades, filename):

        rows = []

        for trade in trades:

            rows.append({

                "Symbol": trade.symbol,
                "Strategy": trade.strategy,

                "Entry Time": trade.entry_time,
                "Exit Time": trade.exit_time,

                "Entry Price": trade.entry_price,
                "Exit Price": trade.exit_price,

                "Quantity": trade.quantity,

                "Gross Profit": trade.gross_profit,
                "Fees": trade.fees,
                "Net Profit": trade.net_profit,

                "Profit %": trade.profit_percent,

                "Duration (Hours)": trade.duration,
                "Exit Reason": trade.exit_reason
            })

        df = pd.DataFrame(rows)

        df.to_csv(filename, index=False)

        return df