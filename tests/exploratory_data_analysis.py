import pytest
import pandas as pd

from src.exploratory_data_analysis import view_column_hist
from utils.enumerations import ColumnNames


def test_work_hours_hist(input_data: pd.DataFrame):

    try:
        view_column_hist(input_data, ColumnNames.HOURS_PER_WEEK.value)

    except Exception as exception:
        pytest.fail('Showing of histogram failed: {}'.format(exception))