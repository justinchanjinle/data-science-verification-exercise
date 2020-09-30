import hashlib
import os


def join_dir(*dir) -> str:
    """
    Joins multiple paths
    :param dir: Directories separated by comma
    :return:
    """
    return os.path.join(*dir)


def get_parent_dir(path: str) -> str:
    """Returns parent directory of the path"""
    return os.path.dirname(path)


def get_abs_dir(path: str) -> str:
    """Returns absolute path"""
    return os.path.abspath(path)


def get_md5(path: str):
    """Retrieve md5 hash of the file"""
    with open(path, 'rb') as file:
        return hashlib.md5(file.read()).hexdigest()

