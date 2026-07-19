from bybit.endpoints.base_endpoint import BaseEndpoint


class AccountEndpoints(BaseEndpoint):

    DEFAULT_ACCOUNT_TYPE = "UNIFIED"

    def get_wallet_balance(
        self,
        account_type: str = DEFAULT_ACCOUNT_TYPE,
        coin: str | None = None,
    ):

        params = {
            "accountType": account_type,
        }

        if coin is not None:
            params["coin"] = coin

        return self.get(
            "/v5/account/wallet-balance",
            params=params,
            auth=True,
        )

    def get_fee_rates(
        self,
        symbol: str | None = None,
        category: str = "linear",
    ):

        params = {
            "category": category,
        }

        if symbol is not None:
            params["symbol"] = symbol

        return self.get(
            "/v5/account/fee-rate",
            params=params,
            auth=True,
        )

    def get_transaction_log(
        self,
        account_type: str = DEFAULT_ACCOUNT_TYPE,
        limit: int = 50,
    ):

        params = {
            "accountType": account_type,
            "limit": limit,
        }

        return self.get(
            "/v5/account/transaction-log",
            params=params,
            auth=True,
        )