from exchange.exchange_balance import ExchangeBalance


class BybitBalanceParser:

    @staticmethod
    def parse(
        response: dict,
    ) -> ExchangeBalance:

        account = response["result"]["list"][0]

        return ExchangeBalance(
            total_equity=float(account["totalEquity"]),
            wallet_balance=float(account["totalWalletBalance"]),
            available_balance=float(account["totalAvailableBalance"]),
        )