import pandas as pd
import numpy as np


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert column names to lowercase, replace spaces with underscores,
    and strip extra whitespace.
    """
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows."""
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    print(f"🧹 Removed {before - after} duplicate rows")
    return df


def fix_whitespace(df: pd.DataFrame) -> pd.DataFrame:
    """
    Strip whitespace from string columns.
    """
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].astype(str).str.strip()
    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic missing value handling:
    - Numeric columns → fill with median
    - String columns → fill with 'Unknown'
    - Date columns → leave as NaT (optional)
    """
    for col in df.columns:
        if df[col].dtype in ["int64", "float64"]:
            median = df[col].median()
            df[col] = df[col].fillna(median)
        elif df[col].dtype == "object":
            df[col] = df[col].replace("nan", np.nan)
            df[col] = df[col].fillna("Unknown")
    return df


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Full cleaning pipeline.
    """
    print("🔧 Cleaning data...")

    df = standardize_column_names(df)
    df = fix_whitespace(df)
    df = remove_duplicates(df)
    df = handle_missing_values(df)

    print("✅ Cleaning complete")
    return df
