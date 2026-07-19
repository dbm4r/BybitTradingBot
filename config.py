import os

from dotenv import load_dotenv

load_dotenv()


# ==========================================
# Environment
# ==========================================

BYBIT_API_KEY = os.getenv(
    "BYBIT_API_KEY",
    "",
)

BYBIT_API_SECRET = os.getenv(
    "BYBIT_API_SECRET",
    "",
)

BYBIT_TESTNET = (
    os.getenv(
        "BYBIT_TESTNET",
        "False",
    ).lower()
    == "true"
)

HTTP_DEBUG = (
    os.getenv(
        "HTTP_DEBUG",
        "True",
    ).lower()
    == "true"
)


# ==========================================
# Defaults
# ==========================================

INITIAL_BALANCE = 10_000

TRADING_FEE = 0.00055