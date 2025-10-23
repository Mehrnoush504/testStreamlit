import streamlit as st
from PIL import Image

# Header
st.header("Image Gallery with Batch Upload")

# Multi-file uploader
uploaded_files = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg", "gif"], accept_multiple_files=True)

if uploaded_files:
    st.subheader("Gallery")
    
    for uploaded_file in uploaded_files:
        # Open image
        image = Image.open(uploaded_file)
        
        # Display image
        st.image(image, caption=f"{uploaded_file.name} ({uploaded_file.type.split('/')[-1]})", use_container_width=True)
        
