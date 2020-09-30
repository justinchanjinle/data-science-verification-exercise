import matplotlib.pyplot as plt
import pandas as pd

from sklearn.metrics import roc_curve

from src.training import get_train_and_test_data, train_model, get_y_probabilities
from utils.enumerations import Directories, Values


def get_roc_metrics(data_table: pd.DataFrame, model):
    """Get fpr, tpr and threshold"""

    X_train, X_test, y_train, y_test = get_train_and_test_data(data_table)

    trained_model = train_model(X_train, y_train, model)

    y_prob = get_y_probabilities(X_test, trained_model)
    y_pos_prob = y_prob[:, 1]

    return roc_curve(y_test, y_pos_prob, pos_label=Values.Y_LABEL_MORE.value)


def plot_roc(fpr, tpr):
    """Plot the ROC curve"""
    plt.plot(fpr, tpr)
    plt.title('Receiver Operating Characteristic (ROC)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')

    plt.savefig(Directories.ROC_CURVE_DIR.value)

    plt.show()
    plt.close()
