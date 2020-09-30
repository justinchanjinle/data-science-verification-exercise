import pandas as pd
import pytest

from src.feature_engineering import hours_per_week_level_feature, half_hours_per_week_feature, \
    apply_hours_per_week_level_feature, get_input_data_with_features
from utils.enumerations import ColumnNames, FeatureNames, FeatureClasses


# Test features -----------------------------------------------------------------------
# Test if features are coded correctly


def test_hours_per_week_level_feature():

    assert hours_per_week_level_feature(10) == FeatureClasses.HOURS_PER_WEEK_LOW.value
    assert hours_per_week_level_feature(40) == FeatureClasses.HOURS_PER_WEEK_MID.value
    assert hours_per_week_level_feature(70) == FeatureClasses.HOURS_PER_WEEK_HIGH.value


def test_half_hours_per_week_feature():

    assert half_hours_per_week_feature(10) == 5.0

# Test joining of features -----------------------------------------------------------------------
# Test if features are joined and filled in correctly


def test_apply_hours_per_week_level_feature(input_data: pd.DataFrame):

    try:
        apply_hours_per_week_level_feature(input_data)

    except Exception as exception:
        pytest.fail('Joining of hours_per_week_level_feature failed: {}'.format(exception))


def test_input_data_with_features(input_data: pd.DataFrame):
    """Test that all features are engineered in the input DataFrame"""

    input_data_with_features = get_input_data_with_features(input_data)
    feature_names_list = [feature.value for feature in FeatureNames]

    # Check that engineered feature columns exist in the data
    assert set(feature_names_list) < set(input_data_with_features.columns)
