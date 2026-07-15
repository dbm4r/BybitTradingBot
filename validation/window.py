from dataclasses import dataclass

import pandas as pd


@dataclass
class Window:

    train: pd.DataFrame

    test: pd.DataFrame