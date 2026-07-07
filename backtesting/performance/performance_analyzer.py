from .profit_metrics import ProfitMetrics
from .trade_metrics import TradeMetrics
from .return_metrics import ReturnMetrics
from .risk_metrics import RiskMetrics


class PerformanceAnalyzer:

    def __init__(
        self,
        trades,
        equity_curve,
        initial_balance,
        final_balance
    ):

        self.trades = trades
        self.equity = equity_curve

        self.initial_balance = initial_balance
        self.final_balance = final_balance

    def summary(self):

        return {

            "Net Profit":
            ProfitMetrics.net_profit(
                self.trades
            ),

            "Gross Profit":
            ProfitMetrics.gross_profit(
                self.trades
            ),

            "Gross Loss":
            ProfitMetrics.gross_loss(
                self.trades
            ),

            "Fees":
            ProfitMetrics.total_fees(
                self.trades
            ),

            "ROI":
            ReturnMetrics.roi(
                self.initial_balance,
                self.final_balance
            ),

            "Trades":
            TradeMetrics.total_trades(
                self.trades
            ),

            "Win Rate":
            TradeMetrics.win_rate(
                self.trades
            ),

            "Max Drawdown":
            RiskMetrics.max_drawdown(
                self.equity
            ),
        }