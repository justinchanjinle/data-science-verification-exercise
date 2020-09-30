import pandas as pd

from utils.enumerations import FeatureNames, FeatureClasses, ColumnNames


# Features --------------------------------------------------------------------
# Implement the function of features here


def hours_per_week_level_feature(hours_per_week: float) -> str:
    if hours_per_week <= FeatureClasses.HOURS_PER_WEEK_LOW_VALUE.value:
        return FeatureClasses.HOURS_PER_WEEK_LOW.value

    elif hours_per_week <= FeatureClasses.HOURS_PER_WEEK_MID_VALUE.value:
        return FeatureClasses.HOURS_PER_WEEK_MID.value

    else:
        return FeatureClasses.HOURS_PER_WEEK_HIGH.value


def half_hours_per_week_feature(hours_per_week: float) -> float:
    return 0.5*hours_per_week


# Apply features -----------------------------------------------------------------
# Join the feature column to the input data here using the apply method

def apply_hours_per_week_level_feature(input_data: pd.DataFrame) -> None:
    input_data[FeatureNames.HOURS_PER_WEEK_LEVEL.value] = input_data[ColumnNames.HOURS_PER_WEEK.value].\
        apply(hours_per_week_level_feature)


def apply_half_hours_per_week_feature(input_data: pd.DataFrame) -> None:
    input_data[FeatureNames.HALF_HOURS_PER_WEEK.value] = input_data[ColumnNames.HOURS_PER_WEEK.value].\
        apply(half_hours_per_week_feature)


# Return table with features -----------------------------------------------------

def get_input_data_with_features(input_data: pd.DataFrame) -> pd.DataFrame:
    """
    Join the features to the input data and returns the new DataFrame
    :param input_data: Input data DataFrame
    :return: DataFrame with features
    """
    apply_hours_per_week_level_feature(input_data)
    apply_half_hours_per_week_feature(input_data)
    return input_data
