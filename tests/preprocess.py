import pandas as pd

from src.preprocess import check_null_values, check_question_mark_as_null, replace_question_mark_with_nan, \
    drop_nan_values
from utils.enumerations import Values


def test_check_question_mark(raw_data: pd.DataFrame):
    """Test that all null values are indicated by the question mark."""

    # Check that there are no pandas null values (NaN) in the raw DataFrame
    assert not check_null_values(raw_data)

    # Check that question mark exists in more than one column
    assert check_question_mark_as_null(raw_data)


def test_replace_question_mark_with_nan(raw_data: pd.DataFrame):
    """Test that all ? has been replaced with NaN successfully"""

    raw_data_nan = replace_question_mark_with_nan(raw_data)

    # Check the existence of NaN values
    assert check_null_values(raw_data_nan)

    # Check that there are no more question marks
    assert not check_question_mark_as_null(raw_data_nan)


def test_dropped_rows(raw_data_nan: pd.DataFrame, raw_data_row_count: int):
    """Test that dropped rows do not exceed 10% of total rows"""

    raw_data_dropped_rows = drop_nan_values(raw_data_nan)
    raw_data_dropped_rows_count = raw_data_dropped_rows.shape[0]

    # Check that rows are being dropped
    assert raw_data_dropped_rows_count < raw_data_row_count

    dropped_rows_count = raw_data_row_count - raw_data_dropped_rows_count
    dropped_rows_percentage = float(dropped_rows_count)/float(raw_data_row_count)

    # Check that dropped rows do not exceed 10%
    assert dropped_rows_percentage < Values.DROPPED_ROWS_THRESHOLD.value
