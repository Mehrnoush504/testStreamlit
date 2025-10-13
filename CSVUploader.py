import streamlit as st
import pandas as pd

# Header
st.header("CSV Uploader & Interactive Table")

# File uploader
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    # Load CSV
    df = pd.read_csv(uploaded_file)
    
    
    # Smaller header
    st.subheader("Data Table")
    
    # Search box
    search_value = st.text_input("Search")
    
    if search_value:
        # Filter rows where any cell matches the search string
        mask = df.apply(lambda row: row.astype(str).str.contains(search_value, case=False).any(), axis=1)
        filtered_df = df[mask]
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
    rows_per_page = st.slider("Selected page (rows per page)", min_value=1, max_value=min(100, len(filtered_df)), value=min(10, len(filtered_df)))
    
    # Display the table
    st.dataframe(filtered_df.head(rows_per_page))
