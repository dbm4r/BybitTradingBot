class Statistics:

    @staticmethod
    def total_profit(trades):
        return sum(trade.net_profit for trade in trades)

    @staticmethod
    def total_trades(trades):
        return len(trades)

    @staticmethod
    def winning_trades(trades):
        return len([trade for trade in trades if trade.net_profit > 0])

    @staticmethod
    def losing_trades(trades):
        return len([trade for trade in trades if trade.net_profit < 0])

    @staticmethod
    def win_rate(trades):
        if len(trades) == 0:
            return 0

        return (
            Statistics.winning_trades(trades)
            / len(trades)
        ) * 100

    @staticmethod
    def average_win(trades):
        wins = [
            trade.net_profit
            for trade in trades
            if trade.net_profit > 0
        ]

        if not wins:
            return 0

        return sum(wins) / len(wins)

    @staticmethod
    def average_loss(trades):
        losses = [
            trade.net_profit
            for trade in trades
            if trade.net_profit < 0
        ]

        if not losses:
            return 0

        return sum(losses) / len(losses)