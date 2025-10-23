# Multi-Tool Streamlit App

A **Streamlit** application that provides three interactive tools in a single interface:  

1. **📝 User Information Form** – Collects user details like name, age, feedback, gender, and weekly activity.  
2. **📊 CSV Uploader & Interactive Table** – Upload CSV files, search numeric values, sort numeric columns, and display data interactively.  
3. **🧮 Image Gallery with Batch Upload** – Upload multiple images and display them.

The app uses a **sidebar navigation** with emojis for easy switching between tools.  

---

## Features

### Sidebar Navigation
- 📝 Form  
- 📊 CSV Uploader  
- 🧮 Image Gallery  
- Default page: Form  

### User Information Form
- Input fields: Name, Age, Feedback  
- Gender selection with radio buttons  
- Weekly activity slider  
- Terms and conditions checkbox  
- Submit button with green success message and summary display  

### CSV Uploader & Interactive Table
- Upload CSV files  
- Search numeric values exactly  
- Sort numeric columns ascending/descending  
- Select number of rows to display per page   

### Image Gallery
- Upload multiple images at once  
- Display images with name and file format  
- Clean gallery layout  

---

## Requirements

| Package            | Version      |
|------------------|------------|
| Python            | 3.10.0     |
| streamlit         | 1.50.0     |
| numpy             | 2.2.6     |
| pandas            | 2.3.3     |
| pillow            | 11.3.0     |


---

## Installation & Running the App


```bash
git clone https://github.com/Mehrnoush504/testStreamlit.git
cd testStreamlit
streamlit run app.py
