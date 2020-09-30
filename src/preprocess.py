import numpy as np
import pandas as pd

from utils.enumerations import Values


def check_null_values(data_table: pd.DataFrame) -> bool:
    """
    Checks if the entire DataFrame contains any null values
    :param data_table: Raw data DataFrame
    :return: bool
    """

    return data_table.isnull().any().any()


def check_question_mark_as_null(data_table: pd.DataFrame) -> bool:
    """
    Checks that at least one column has ? value
    :param data_table: Raw data DataFrame
    :return: bool
    """

    return any([Values.RAW_DATA_NULL.value in set(data_table[column_value]) for column_value in data_table])


def replace_question_mark_with_nan(data_table: pd.DataFrame) -> pd.DataFrame:
    """
    Replace question mark with NaN
    :return: None
    """
    return data_table.replace(Values.RAW_DATA_NULL.value, np.nan)


def drop_nan_values(data_table: pd.DataFrame) -> pd.DataFrame:
    """
    Drops rows with NaN values
    :param data_table: DataFrame
    :return: DataFrame with dropped NaN rows
    """
    return data_table.dropna()
