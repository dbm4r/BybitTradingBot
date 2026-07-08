from itertools import product


class ParameterGrid:

    def __init__(
        self,
        **parameters
    ):

        self.parameters = parameters

    def generate(self):

        keys = list(
            self.parameters.keys()
        )

        values = list(
            self.parameters.values()
        )

        for combination in product(*values):

            yield dict(
                zip(
                    keys,
                    combination
                )
            )