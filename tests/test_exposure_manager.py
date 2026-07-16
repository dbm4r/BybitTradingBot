from portfolio.asset_registry import AssetRegistry
from portfolio.exposure_manager import ExposureManager

assets = AssetRegistry()

print("========== EXPOSURE MANAGER ==========\n")

print(
    "Open Positions:",
    ExposureManager.open_positions(
        assets
    ),
)

print()

print(
    "BTC Position:",
    ExposureManager.has_open_position(
        assets,
        "BTCUSDT",
    ),
)