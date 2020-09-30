import pandas as pd
import pytest

from src.training import get_features_data, get_label_data, get_train_and_test_data, train_model

from utils.enumerations import ColumnNames, Models, Values


def test_labels_and_features(input_data_features: pd.DataFrame):

    y_label = get_label_data(input_data_features)
    x_features = get_features_data(input_data_features)

    # check that y label is correct
    assert isinstance(y_label, pd.Series)
    assert set(y_label) == {Values.Y_LABEL_LESS.value, Values.Y_LABEL_MORE.value}

    # Check that y label has been removed from features
    assert ColumnNames.INCOME.value not in x_features.columns


def test_train_random_forest_model(input_data_features: pd.DataFrame):
    """Tests that random forest model training works"""
    X_train, X_test, y_train, y_test = get_train_and_test_data(input_data_features)

    model = Models.RANDOM_FOREST.value

    try:

        trained_model = train_model(X_train, y_train, model)

    except Exception as exception:
        pytest.fail('Failed to train model: {}'.format(exception))
