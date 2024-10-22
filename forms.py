import pandas as pd
import numpy as np
import matplotlib as plt
import streamlit as st
from datetime import datetime
from constants import Skills

st.title("Form Details")

form_values = {
    "name": None,
    "age": None,
    "gender": None,
    "dob": None,
    "location": None,
    "designation": None,
    "expected_ctc": None,
    "current_ctc": None,
    "experience": None,
    "skill_set": [],
}

min_date = datetime(1975, 1, 1)
max_date = datetime.now()

# including it inside with, because we dont want to
# rerun again & again when any elemtn value changes,
# so group it under form
with st.form(key='user_info_form', clear_on_submit=True):     # filling key is a good practice
    form_values['name'] = st.text_input("Enter your Name")
    dob = st.date_input("Enter your DOB", min_value=min_date, max_value=max_date)

    age = 0
    if form_values['dob']:
        age = max_date.year - dob.year
        if age < 21:
            st.warning("Not Eligible.")
        st.write(f"Age is {age}.")

    form_values['dob'] = age
    form_values['gender'] = st.selectbox("Gender", ["Male", "Female"])
    form_values['qualification'] = st.selectbox("Enter your Qualification", ["Bachelors", "Masters", "Diploma", "PUC", "Certification"])
    form_values['doq'] = st.date_input("Enter Date of Qualification", min_value=min_date, max_value=max_date)
    form_values['location'] = st.text_input("Enter Coordinates")
    form_values['designation'] = st.text_input("Enter Designation")
    form_values['expected_ctc'] = st.number_input("Enter Expected CTC")
    form_values['current_ctc'] = st.number_input("Enter current CTC")
    form_values['experience'] = st.select_slider("Enter Experience", options=list(range(30)))
    form_values['skill_set'] = st.multiselect("Enter Skills", [skill.name for skill in Skills])

    submit_btn = st.form_submit_button(label="Submit Details")
    if submit_btn:
        # Warning message
        if not all(form_values.values()):
            st.warning("Please fill in all Fields.")
        else:
            form_data = pd.DataFrame(form_values)