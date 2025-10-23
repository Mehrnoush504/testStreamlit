import streamlit as st
import pandas as pd
import numpy as np

# Header
st.header("CSV Uploader & Interactive Table")

# --- Cached CSV loader ---
@st.cache_data
def load_csv(file):
    return pd.read_csv(file)

# File uploader
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    # Load CSV (cached)
    df = load_csv(uploaded_file)
    
    # Smaller header
    st.subheader("Data Table")
    
    # Numeric input for search
    search_value = st.text_input("Enter a number to search", value="")
    
    # Check if user entered something and pressed Enter
    if search_value.strip():
        try:
            search_value = float(search_value)
            # Select only numeric columns
            numeric_df = df.select_dtypes(include=["number"])
            # Filter rows where at least one numeric column matches the search value
            mask = numeric_df.apply(lambda row: np.isclose(row, search_value, atol=1e-8).any(), axis=1)
            filtered_df = df[mask]
        except ValueError:
            st.warning("Please enter a valid numeric value.")
            filtered_df = df.copy()
    else:
        filtered_df = df.copy()
    
    # Dropdown to sort numeric columns
    numeric_cols = filtered_df.select_dtypes(include=['number']).columns.tolist()
    if numeric_cols:
        sort_col = st.selectbox("Sort by column", ["None"] + numeric_cols)
        if sort_col != "None":
            sort_order = st.radio("Sort order", ["Ascending", "Descending"])
            ascending = True if sort_order == "Ascending" else False
            filtered_df = filtered_df.sort_values(by=sort_col, ascending=ascending)
    
    # Slider for rows per page
    rows_per_page = st.slider(
        "Rows per page",
        min_value=1,
        max_value=min(100, len(filtered_df)),
        value=min(10, len(filtered_df))
    )
    
    # Display the table
    st.dataframe(filtered_df.head(rows_per_page))
