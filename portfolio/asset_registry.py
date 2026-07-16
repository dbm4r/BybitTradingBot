from dataclasses import dataclass, field
from collections.abc import Iterator

from portfolio.asset_context import AssetContext


@dataclass(slots=True)
class AssetRegistry:

    assets: dict[str, AssetContext] = field(
        default_factory=dict
    )

    def add(
        self,
        asset: AssetContext,
    ) -> None:

        if asset.symbol in self.assets:
            raise ValueError(
                f"Asset '{asset.symbol}' is already registered."
            )

        self.assets[asset.symbol] = asset

    def get(
        self,
        symbol: str,
    ) -> AssetContext:

        if symbol not in self.assets:
            raise KeyError(
                f"Unknown asset '{symbol}'."
            )

        return self.assets[symbol]

    def remove(
        self,
        symbol: str,
    ) -> None:

        if symbol not in self.assets:
            raise KeyError(
                f"Unknown asset '{symbol}'."
            )

        del self.assets[symbol]

    def exists(
        self,
        symbol: str,
    ) -> bool:

        return symbol in self.assets

    def clear(
        self,
    ) -> None:

        self.assets.clear()

    @property
    def symbols(
        self,
    ) -> tuple[str, ...]:

        return tuple(
            sorted(self.assets.keys())
        )

    @property
    def count(
        self,
    ) -> int:

        return len(
            self.assets
        )

    def values(
        self,
    ) -> tuple[AssetContext, ...]:

        return tuple(
            self.assets.values()
        )

    def items(
        self,
    ) -> tuple[tuple[str, AssetContext], ...]:

        return tuple(
            self.assets.items()
        )

    def __contains__(
        self,
        symbol: str,
    ) -> bool:

        return symbol in self.assets

    def __iter__(
        self,
    ) -> Iterator[AssetContext]:

        return iter(
            self.assets.values()
        )

    def __len__(
        self,
    ) -> int:

        return len(
            self.assets
        )