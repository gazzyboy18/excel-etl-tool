import os
import pandas as pd


class FileLoadError(Exception):
    """Custom exception for file loading issues."""
    pass


def load_file(file_path: str) -> pd.DataFrame:
    """
    Load an Excel or CSV file into a pandas DataFrame.

    Supports:
    - .xlsx, .xls (Excel)
    - .csv

    Raises:
        FileLoadError: if file doesn't exist or format not supported.
    """
    if not os.path.exists(file_path):
        raise FileLoadError(f"File not found: {file_path}")

    _, ext = os.path.splitext(file_path)
    ext = ext.lower()

    try:
        if ext in [".xlsx", ".xls"]:
            df = pd.read_excel(file_path)
        elif ext == ".csv":
            df = pd.read_csv(file_path)
        else:
            raise FileLoadError(f"Unsupported file type: {ext}")
    except Exception as e:
        raise FileLoadError(f"Error loading file: {e}")

    if df.empty:
        raise FileLoadError("File loaded but DataFrame is empty.")

    return df
