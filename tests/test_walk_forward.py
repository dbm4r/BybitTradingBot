from core.config import Config
from core.settings import Settings
from data.data_manager import DataManager
from optimization.parameter_grid import ParameterGrid
from validation.walk_forward import WalkForwardValidator


config = Config()

manager = DataManager()

dataframe = manager.download_historical_data(
    symbol=config.symbol,
    interval=config.interval,
    limit=500,
)

validator = WalkForwardValidator(
    settings=Settings(),
    symbol=config.symbol,
)

validator.validate(
    dataframe=dataframe,
    strategy_name="SMA",
    parameter_grid=ParameterGrid(
        fast_period=[10, 20],
        slow_period=[50, 100],
    ),
    train_size=300,
    test_size=100,
)