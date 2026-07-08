from indicators.moving_average import SimpleMovingAverage


class IndicatorFactory:

    _indicators = {
        "SMA": SimpleMovingAverage,
    }

    @classmethod
    def create(
        cls,
        name: str,
        **kwargs
    ):

        if name not in cls._indicators:

            raise ValueError(
                f"Unknown indicator: {name}"
            )

        return cls._indicators[name](**kwargs)