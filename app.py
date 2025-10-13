import streamlit as st
import runpy

# Sidebar with emoji options
# st.sidebar.title("Navigation")
app_choice = st.sidebar.radio(
    "Choose an Option",
    [
        "📝 Form",
        "📊 CSV Uploader",
        "🧮 Image Gallery"
    ],
    index=0  # Default to Form
)

# Mapping of radio options to .py file names
app_files = {
    "📝 Form": "Form.py",
    "📊 CSV Uploader": "CSVUploader.py",
    "🧮 Image Gallery": "ImageGallery.py"
}

# Run the selected app
selected_file = app_files[app_choice]
runpy.run_path(selected_file)
