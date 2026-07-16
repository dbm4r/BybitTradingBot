from portfolio.asset_registry import AssetRegistry


class ExposureManager:

    @staticmethod
    def open_positions(
        assets: AssetRegistry,
    ) -> int:

        count = 0

        for asset in assets:

            if asset.engine.portfolio.in_position(
                asset.symbol
            ):
                count += 1

        return count

    @staticmethod
    def has_open_position(
        assets: AssetRegistry,
        symbol: str,
    ) -> bool:

        if not assets.exists(symbol):
            return False

        asset = assets.get(symbol)

        return asset.engine.portfolio.in_position(
            symbol
        )