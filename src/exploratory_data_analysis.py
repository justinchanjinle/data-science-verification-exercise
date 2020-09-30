import pandas as pd

import matplotlib.pyplot as plt

from utils.enumerations import FolderNames
from utils.helpers import get_parent_dir, get_abs_dir, join_dir


def view_column_hist(data_table: pd.DataFrame, column: str) -> None:
    """Plots and saves the column's histogram"""
    data_table.hist(column=column)
    file_name = '{}.svg'.format(column)
    file_path = join_dir(get_parent_dir(get_parent_dir(get_abs_dir(__file__))), FolderNames.FIGURES.value, file_name)
    plt.savefig(file_path)
    plt.show()
    plt.close()
