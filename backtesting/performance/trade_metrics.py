class TradeMetrics:

    @staticmethod
    def total_trades(trades):

        return len(trades)

    @staticmethod
    def winning_trades(trades):

        return len([
            t
            for t in trades
            if t.net_profit > 0
        ])

    @staticmethod
    def losing_trades(trades):

        return len([
            t
            for t in trades
            if t.net_profit < 0
        ])

    @staticmethod
    def win_rate(trades):

        if len(trades) == 0:
            return 0

        return (
            TradeMetrics.winning_trades(trades)
            / len(trades)
        ) * 100