import pytest

from src.ingest_data import ingest_csv_from_zipfile

from utils.enumerations import FileNames, Directories


def test_ingest_zipfile():
    """Tests that ingest_csv_from_zipfile works and inspect the DataFrame with debugging feature.
    What do you we know from inspection?"""

    try:

        adult_data_df = ingest_csv_from_zipfile(Directories.ZIP_FILE_DIR.value, FileNames.DATA_FILE.value)

    except Exception as exception:

        pytest.fail('Ingest zip file error: {}'.format(exception))

    pass
