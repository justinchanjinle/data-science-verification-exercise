import pandas as pd

from typing import List

from utils.enumerations import ColumnNames
from sklearn.model_selection import train_test_split


def get_label_data(data_table: pd.DataFrame) -> pd.Series:
    return data_table[ColumnNames.INCOME.value]


def get_features_data(data_table: pd.DataFrame):
    return data_table.drop(ColumnNames.INCOME.value, axis=1, errors='ignore')


def get_train_and_test_data(data_table: pd.DataFrame):
    """Returns X_train, X_test, y_train, y_test"""

    y_label = get_label_data(data_table)
    x_features = get_features_data(data_table)

    # Convert categorical data to one-hot
    x_dummy_features = pd.get_dummies(x_features)

    return train_test_split(x_dummy_features, y_label, random_state=0)


def train_model(X_train: List, y_train: List, model):
    return model.fit(X_train, y_train)


def get_y_predicted(X_test, model):
    return model.predict(X_test)


def get_y_probabilities(X_test, model):
    return model.predict_proba(X_test)

