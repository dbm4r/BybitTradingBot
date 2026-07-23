class TradingCyclePipeline:

    def __init__(
        self,
        stages,
    ):

        self._stages = list(
            stages,
        )

    def execute(
        self,
        context,
    ):

        current = context

        for stage in self._stages:

            current = stage.execute(
                current,
            )

        return current

    @property
    def stages(
        self,
    ):

        return tuple(
            self._stages,
        )