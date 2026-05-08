import streamlit as st
import pandas as pd
from io import BytesIO

from etl_app.loader import load_file
from etl_app.cleaner import clean_dataframe
from etl_app.analyzer import (
    missing_value_report,
    summary_statistics,
    detect_outliers,
    correlation_matrix
)
from etl_app.exporter import (
    generate_text_report,
    generate_html_report
)


st.set_page_config(page_title="Excel Cleaner & Analyzer", layout="wide")

st.title("📊 Excel/CSV Data Cleaner & Analyzer")
st.write("Upload your file and let the system clean, analyze, and generate reports.")


# -----------------------------
# File Upload Section
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload Excel or CSV file",
    type=["xlsx", "xls", "csv"]
)

if uploaded_file:
    st.success("File uploaded successfully!")

    # Load file into DataFrame
    df = pd.read_excel(uploaded_file) if uploaded_file.name.endswith(("xlsx", "xls")) else pd.read_csv(uploaded_file)

    st.subheader("📂 Raw Data Preview")
    st.dataframe(df.head())

    # Clean data
    st.subheader("🧼 Cleaning Data...")
    cleaned_df = clean_dataframe(df)
    st.dataframe(cleaned_df.head())

    # Analysis
    st.subheader("📉 Missing Value Report")
    mv = missing_value_report(cleaned_df)
    st.dataframe(mv)

    st.subheader("📊 Summary Statistics")
    stats = summary_statistics(cleaned_df)
    st.dataframe(stats)

    st.subheader("🚨 Outliers Detected")
    outliers = detect_outliers(cleaned_df)
    if outliers.empty:
        st.info("No significant outliers found")
    else:
        st.dataframe(outliers)

    st.subheader("🔗 Correlation Matrix")
    corr = correlation_matrix(cleaned_df)
    st.dataframe(corr)

    # -----------------------------
    # Download Cleaned Excel
    # -----------------------------
    st.subheader("💾 Download Cleaned File")

    buffer = BytesIO()
    cleaned_df.to_excel(buffer, index=False)
    buffer.seek(0)

    st.download_button(
        label="Download Cleaned Excel",
        data=buffer,
        file_name="cleaned_data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    # -----------------------------
    # Generate Reports
    # -----------------------------
    st.subheader("📝 Download Reports")

    # Text report
    generate_text_report(mv, stats, outliers, corr, "analysis_report.txt")
    with open("analysis_report.txt", "rb") as f:
        st.download_button(
            label="Download Text Report",
            data=f,
            file_name="analysis_report.txt",
            mime="text/plain"
        )

    # HTML report
    generate_html_report(mv, stats, outliers, corr, "analysis_report.html")
    with open("analysis_report.html", "rb") as f:
        st.download_button(
            label="Download HTML Report",
            data=f,
            file_name="analysis_report.html",
            mime="text/html"
        )
