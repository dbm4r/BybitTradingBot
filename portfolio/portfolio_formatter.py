from portfolio.portfolio_report import (
    PortfolioReport,
)


class PortfolioFormatter:

    @staticmethod
    def format(
        report: PortfolioReport,
    ) -> str:

        lines = [
            "=" * 42,
            "PORTFOLIO REPORT",
            "=" * 42,
            "",
            f"Timestamp          : {report.timestamp}",
            "",
            f"Portfolio Value    : ${report.portfolio_value:,.2f}",
            f"Cash               : ${report.cash:,.2f}",
            f"Invested Capital   : ${report.invested_capital:,.2f}",
            "",
            f"Open Positions     : {report.open_positions}",
            "",
            f"Return             : {report.total_return_percent:.2f}%",
            f"Capital Usage      : {report.capital_utilization_percent:.2f}%",
            f"Fees               : {report.fee_percent:.2f}%",
            "",
            "=" * 42,
        ]

        return "\n".join(lines)