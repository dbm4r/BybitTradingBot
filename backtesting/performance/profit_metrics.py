class ProfitMetrics:

    @staticmethod
    def gross_profit(trades):

        return sum(
            trade.gross_profit
            for trade in trades
            if trade.gross_profit > 0
        )

    @staticmethod
    def gross_loss(trades):

        return abs(sum(
            trade.gross_profit
            for trade in trades
            if trade.gross_profit < 0
        ))

    @staticmethod
    def net_profit(trades):

        return sum(
            trade.net_profit
            for trade in trades
        )

    @staticmethod
    def total_fees(trades):

        return sum(
            trade.fees
            for trade in trades
        )