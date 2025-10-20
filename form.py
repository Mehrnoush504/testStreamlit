import streamlit as st

# Header
st.header("User Information Form")

# Form inputs
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=150, step=1)
feedback = st.text_area("Your feedback")
terms = st.checkbox("I accept the terms and conditions")
gender = st.radio("Gender", ["Male", "Female", "Other"])
days_per_week = st.slider("How many days do you work per week?", min_value=1, max_value=7, value=5)

# Submit button
if st.button("Submit"):
    if name:
        st.success(f"Thank you for submitting, {name}!")
        st.write(f"Age: {age}")
        st.write(f"Feedback: {feedback}")
        st.write(f"Gender: {gender}")
        st.write(f"Days active per week: {days_per_week}")
        if terms:
            st.write("You have accepted the terms and conditions")
        else:
            st.write("You did not accept the terms and conditions")
    else:
        st.error("Please enter your name before submitting.")
