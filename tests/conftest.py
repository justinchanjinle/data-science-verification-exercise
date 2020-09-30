import pandas as pd
import pytest

from utils.enumerations import FileNames, Directories

from src.feature_engineering import get_input_data_with_features
from src.ingest_data import ingest_csv_from_zipfile
from src.preprocess import replace_question_mark_with_nan, drop_nan_values


@pytest.fixture(scope='module')
def raw_data() -> pd.DataFrame:
    return ingest_csv_from_zipfile(Directories.ZIP_FILE_DIR.value, FileNames.DATA_FILE.value)


@pytest.fixture(scope='module')
def raw_data_nan(raw_data: pd.DataFrame) -> pd.DataFrame:
    return replace_question_mark_with_nan(raw_data)


@pytest.fixture(scope='module')
def input_data(raw_data_nan: pd.DataFrame) -> pd.DataFrame:
    """Data after dropping NaN values"""
    return drop_nan_values(raw_data_nan)


@pytest.fixture(scope='module')
def raw_data_row_count(raw_data: pd.DataFrame) -> pd.DataFrame:
    """Fixture for row count of the raw data"""
    return raw_data.shape[0]


@pytest.fixture(scope='module')
def input_data_features(input_data: pd.DataFrame):
    return get_input_data_with_features(input_data)

