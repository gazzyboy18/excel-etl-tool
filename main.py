import argparse
from etl_app.loader import load_file, FileLoadError
from etl_app.cleaner import clean_dataframe
from etl_app.analyzer import (
    missing_value_report,
    summary_statistics,
    detect_outliers,
    correlation_matrix
)
from etl_app.exporter import (
    save_cleaned_excel,
    generate_text_report,
    generate_html_report
)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Excel/CSV Data Cleaner, Analyzer & Report Generator"
    )

    parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="Path to the input Excel/CSV file"
    )

    parser.add_argument(
        "--output",
        "-o",
        required=False,
        help="Optional: path to save cleaned Excel file"
    )

    return parser.parse_args()


def main():
    args = parse_args()

    print("📂 Loading file...")
    try:
        df = load_file(args.input)
        print(f"✅ Loaded successfully: {df.shape[0]} rows, {df.shape[1]} columns")
    except FileLoadError as e:
        print(f"❌ Error: {e}")
        return

    print("\n🧼 Cleaning data...")
    df = clean_dataframe(df)

    print("\n📊 Preview of cleaned data:")
    print(df.head())

    print("\n📉 Missing Value Report:")
    mv_report = missing_value_report(df)
    print(mv_report)

    print("\n📊 Summary Statistics:")
    stats_report = summary_statistics(df)
    print(stats_report)

    print("\n🚨 Outliers Detected:")
    outlier_rows = detect_outliers(df)
    print(outlier_rows if not outlier_rows.empty else "No significant outliers found")

    print("\n🔗 Correlation Matrix:")
    corr_report = correlation_matrix(df)
    print(corr_report)

    # Export section
    if args.output:
        print(f"\n💾 Saving cleaned Excel to: {args.output}")
        save_cleaned_excel(df, args.output)

        print("\n📝 Generating text report...")
        generate_text_report(
            mv_report,
            stats_report,
            outlier_rows,
            corr_report,
            "analysis_report.txt"
        )

        print("\n🌐 Generating HTML report...")
        generate_html_report(
            mv_report,
            stats_report,
            outlier_rows,
            corr_report,
            "analysis_report.html"
        )

    print("\n🎉 ETL + Analysis + Export complete!")


if __name__ == "__main__":
    main()
