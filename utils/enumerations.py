import numpy as np

from enum import Enum

from sklearn.ensemble import RandomForestClassifier
from utils.helpers import get_parent_dir, get_abs_dir, join_dir


class FileNames(Enum):

    ZIP_FILE = 'adult-income-dataset.zip'
    DATA_FILE = 'adult.csv'
    ROC_CURVE = 'roc_curve.png'


class FolderNames(Enum):
    FIGURES = 'figures'


class Values(Enum):

    RAW_DATA_NULL = '?'
    NULL_VALUES = np.nan
    DROPPED_ROWS_THRESHOLD = 0.1
    Y_LABEL_MORE = '>50K'
    Y_LABEL_LESS = '<=50K'


class ColumnNames(Enum):
    HOURS_PER_WEEK = 'hours-per-week'
    INCOME = 'income'


class FeatureNames(Enum):
    HOURS_PER_WEEK_LEVEL = 'hours-per-week-level'
    HALF_HOURS_PER_WEEK = 'half-hours-per-week'


class FeatureClasses(Enum):
    HOURS_PER_WEEK_LOW_VALUE = 30.0
    HOURS_PER_WEEK_MID_VALUE = 60.0

    HOURS_PER_WEEK_LOW = 'Low'
    HOURS_PER_WEEK_MID = 'Medium'
    HOURS_PER_WEEK_HIGH = 'High'


class Models(Enum):

    RANDOM_FOREST = RandomForestClassifier(max_depth=20, random_state=0, n_estimators=100, n_jobs=6)


class Directories(Enum):

    ZIP_FILE_DIR = join_dir(get_parent_dir(get_parent_dir(get_abs_dir(__file__))), 'data',
                            FileNames.ZIP_FILE.value)

    ROC_CURVE_DIR = join_dir(get_parent_dir(get_parent_dir(get_abs_dir(__file__))), FolderNames.FIGURES.value,
                             FileNames.ROC_CURVE.value)


class Checksum(Enum):

    ROC_CURVE_MD5 = '90b2ea1c8014212fa1aedef2795a9537'
