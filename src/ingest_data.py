import pandas as pd
import zipfile


def ingest_csv_from_zipfile(zip_file_dir: str, csv_file: str) -> pd.DataFrame:
    """
    Ingest the csv file from the zipfile as DataFrame
    :param zip_file_dir: Directory of zipfile
    :param csv_file: csv file name
    :return: DataFrame of the csv
    """

    with zipfile.ZipFile(zip_file_dir) as zip_files:
        with zip_files.open(csv_file) as csv_table:
            csv_df = pd.read_csv(csv_table, index_col=False)
    return csv_df
