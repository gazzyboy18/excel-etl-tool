import pandas as pd
import numpy as np


def missing_value_report(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a table showing missing value counts and percentages.
    """
    missing_counts = df.isnull().sum()
    missing_percent = (df.isnull().sum() / len(df)) * 100

    report = pd.DataFrame({
        "missing_count": missing_counts,
        "missing_percent": missing_percent.round(2)
    })

    return report


def summary_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns descriptive statistics for numeric columns.
    """
    return df.describe().T


def detect_outliers(df: pd.DataFrame, z_threshold: float = 3.0) -> pd.DataFrame:
    """
    Detect outliers using Z-score method.
    Returns a DataFrame listing outlier rows.
    """
    numeric_df = df.select_dtypes(include=[np.number])

    if numeric_df.empty:
        return pd.DataFrame()

    z_scores = (numeric_df - numeric_df.mean()) / numeric_df.std()
    outlier_mask = (np.abs(z_scores) > z_threshold).any(axis=1)

    return df[outlier_mask]


def correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns correlation matrix for numeric columns.
    """
    numeric_df = df.select_dtypes(include=[np.number])
    if numeric_df.empty:
        return pd.DataFrame()
    return numeric_df.corr()
