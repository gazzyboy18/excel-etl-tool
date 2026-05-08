import pandas as pd
from datetime import datetime


def save_cleaned_excel(df: pd.DataFrame, output_path: str):
    """
    Save cleaned DataFrame to an Excel file.
    """
    df.to_excel(output_path, index=False)
    print(f"💾 Cleaned Excel saved to: {output_path}")


def generate_text_report(
    missing_report: pd.DataFrame,
    summary_stats: pd.DataFrame,
    outliers: pd.DataFrame,
    corr_matrix: pd.DataFrame,
    output_path: str
):
    """
    Generate a plain text analysis report.
    """
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("=== DATA ANALYSIS REPORT ===\n")
        f.write(f"Generated: {datetime.now()}\n\n")

        f.write("=== Missing Value Report ===\n")
        f.write(missing_report.to_string())
        f.write("\n\n")

        f.write("=== Summary Statistics ===\n")
        f.write(summary_stats.to_string())
        f.write("\n\n")

        f.write("=== Outliers Detected ===\n")
        if outliers.empty:
            f.write("No significant outliers found.\n")
        else:
            f.write(outliers.to_string())
        f.write("\n\n")

        f.write("=== Correlation Matrix ===\n")
        f.write(corr_matrix.to_string())
        f.write("\n")

    print(f"📝 Text report saved to: {output_path}")


def generate_html_report(
    missing_report: pd.DataFrame,
    summary_stats: pd.DataFrame,
    outliers: pd.DataFrame,
    corr_matrix: pd.DataFrame,
    output_path: str
):
    """
    Generate a clean HTML report.
    """
    html = f"""
    <html>
    <head>
        <title>Data Analysis Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; padding: 20px; }}
            h2 {{ color: #2c3e50; }}
            table {{ border-collapse: collapse; width: 100%; margin-bottom: 20px; }}
            th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
            th {{ background-color: #f4f4f4; }}
        </style>
    </head>
    <body>
        <h1>Data Analysis Report</h1>
        <p>Generated: {datetime.now()}</p>

        <h2>Missing Value Report</h2>
        {missing_report.to_html()}

        <h2>Summary Statistics</h2>
        {summary_stats.to_html()}

        <h2>Outliers Detected</h2>
        {"<p>No significant outliers found.</p>" if outliers.empty else outliers.to_html()}

        <h2>Correlation Matrix</h2>
        {corr_matrix.to_html()}
    </body>
    </html>
    """

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"🌐 HTML report saved to: {output_path}")
