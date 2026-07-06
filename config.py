import os
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# Read API credentials
BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET")

# Demo or live account
BYBIT_TESTNET = os.getenv("BYBIT_TESTNET", "False").lower() == "true"

# Trading Settings
INITIAL_BALANCE = 10000

# Bybit taker fee (0.055%)
TRADING_FEE = 0.00055