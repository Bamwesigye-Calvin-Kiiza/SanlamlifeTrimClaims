import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.title("📅 Data Trimmer by Created On Date")

# File uploader
uploaded_file = st.file_uploader("Upload your data file (CSV or Excel)", type=["csv", "xlsx"])

if uploaded_file:
    # Load file
    file_extension = uploaded_file.name.split('.')[-1]
    if file_extension == "csv":
        df = pd.read_csv(uploaded_file, parse_dates=["Create_Date"])
    else:
        df = pd.read_excel(uploaded_file, parse_dates=["Create_Date"])

    if "Create_Date" not in df.columns:
        st.error("The uploaded file must contain a 'Create_Date' column.")
    else:
        # Show a sample of the data
        st.write("📋 Sample of data:", df.head())

        # Start date input
        start_date = st.date_input("Select a start date to trim data")

        if start_date:
            # Trim data
            filtered_df = df[df["Create_Date"] >= pd.to_datetime(start_date)]

            if filtered_df.empty:
                st.warning("No data retained after trimming with selected date.")
            else:
                # Display retained range
                min_date = filtered_df["Create_Date"].min().date()
                max_date = filtered_df["Create_Date"].max().date()

                st.success(f"📅 Retained data from {min_date} to {max_date}")
                st.write("🔍 Retained Data Preview:", filtered_df.head())

                # Save filtered data
                output_dir = "C:/Users/calvin.bamwesigye/Downloads/trimmed_data/"
                os.makedirs(output_dir, exist_ok=True)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_path = os.path.join(output_dir, f"trimmed_data_{timestamp}.xlsx")

                filtered_df.to_excel(output_path, index=False)
                st.success(f"✅ Data saved at: `{output_path}`")

                # Optional: Provide download link
                with open(output_path, "rb") as f:
                    st.download_button("📥 Download Trimmed Excel", f, file_name=f"trimmed_data_{timestamp}.xlsx")
