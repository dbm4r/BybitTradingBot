from bybit.parsers.balance_parser import (
    BybitBalanceParser,
)

from exchange.exchange_balance import (
    ExchangeBalance,
)


def test_parse_balance():

    response = {
        "result": {
            "list": [
                {
                    "totalEquity": "10500.25",
                    "totalWalletBalance": "10000.50",
                    "totalAvailableBalance": "9750.75",
                }
            ]
        }
    }

    balance = BybitBalanceParser.parse(
        response
    )

    assert isinstance(
        balance,
        ExchangeBalance,
    )

    assert balance.total_equity == 10500.25

    assert balance.wallet_balance == 10000.50

    assert balance.available_balance == 9750.75


def test_balance_string():

    balance = ExchangeBalance(
        total_equity=10500.25,
        wallet_balance=10000.50,
        available_balance=9750.75,
    )

    expected = (
        "Total Equity      : 10500.25\n"
        "Wallet Balance    : 10000.50\n"
        "Available Balance : 9750.75"
    )

    assert str(balance) == expected