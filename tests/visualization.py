import pandas as pd
import pytest

from src.visualization import  get_roc_metrics, plot_roc

from utils.enumerations import Models, Directories, Checksum
from utils.helpers import get_md5


def test_plot_roc(input_data_features: pd.DataFrame):
    """Test for executability and reproducibility"""

    model = Models.RANDOM_FOREST.value

    try:

        fpr, tpr, threshold = get_roc_metrics(input_data_features, model)
        plot_roc(fpr, tpr)

    except Exception as exception:
        pytest.fail('Plotting of roc curve failed: {}'.format(exception))

    roc_curve_md5 = get_md5(Directories.ROC_CURVE_DIR.value)

    assert roc_curve_md5 == Checksum.ROC_CURVE_MD5.value
