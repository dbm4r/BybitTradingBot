from strategies.framework.base_strategy import BaseStrategy
from strategies.registry.strategy_metadata import (
    StrategyMetadata,
)
from strategies.registry.strategy_registration import (
    StrategyRegistration,
)


class StrategyRegistry:

    def __init__(self):

        self._registrations: dict[
            str,
            StrategyRegistration,
        ] = {}

    def register(
        self,
        strategy: BaseStrategy,
        metadata: StrategyMetadata,
    ) -> None:

        if metadata.name in self._registrations:

            raise ValueError(
                f"Strategy '{metadata.name}' is already registered."
            )

        self._registrations[
            metadata.name
        ] = StrategyRegistration(
            metadata=metadata,
            strategy=strategy,
        )

    def unregister(
        self,
        name: str,
    ) -> None:

        self._registrations.pop(
            name,
            None,
        )

    def contains(
        self,
        name: str,
    ) -> bool:

        return (
            name
            in self._registrations
        )

    def get(
        self,
        name: str,
    ) -> BaseStrategy:

        return self._registrations[
            name
        ].strategy

    def registration(
        self,
        name: str,
    ) -> StrategyRegistration:

        return self._registrations[
            name
        ]

    def metadata(
        self,
        name: str,
    ) -> StrategyMetadata:

        return self._registrations[
            name
        ].metadata

    def registrations(
        self,
    ) -> tuple[
        StrategyRegistration,
        ...
    ]:

        return tuple(
            self._registrations.values()
        )

    def strategies(
        self,
    ) -> tuple[
        BaseStrategy,
        ...
    ]:

        return tuple(

            registration.strategy

            for registration in self._registrations.values()
        )

    def all_metadata(
        self,
    ) -> tuple[
        StrategyMetadata,
        ...
    ]:

        return tuple(

            registration.metadata

            for registration in self._registrations.values()
        )

    def enabled(
        self,
    ) -> tuple[
        StrategyRegistration,
        ...
    ]:

        return tuple(

            registration

            for registration in self._registrations.values()

            if registration.metadata.enabled
        )

    def by_category(
        self,
        category: str,
    ) -> tuple[
        StrategyRegistration,
        ...
    ]:

        return tuple(

            registration

            for registration in self._registrations.values()

            if registration.metadata.category == category
        )

    def by_tag(
        self,
        tag: str,
    ) -> tuple[
        StrategyRegistration,
        ...
    ]:

        return tuple(

            registration

            for registration in self._registrations.values()

            if tag in registration.metadata.tags
        )

    def clear(
        self,
    ) -> None:

        self._registrations.clear()

    @property
    def count(
        self,
    ) -> int:

        return len(
            self._registrations
        )