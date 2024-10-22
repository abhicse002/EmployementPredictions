import pandas as pd
import numpy as np
import matplotlib as plt
import streamlit as st
from datetime import datetime


st.sidebar.title("Subscribe to our Job Notifications.")
st.sidebar.write("Will keep you posted about new Open Positions.")
sidebar_ip = st.sidebar.text_input("Enter Email")


tab1, tab2, tab3, tab4 = st.tabs(["Fill Form", "Charts", "Analysis", "About"])
with tab1:
    st.write("Please fill the Form")

with tab2:
    st.write("Charts")

with tab3:
    st.write("Analysis")

with tab4:
    st.write("About")


# Columns layout, adds Rows with Columns
col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("Content 1")

with col2:
    st.header("Column 2")
    st.write("Content 2")


# Container Example
with st.container(border=True):
    st.write("Container")
    st.write("Grping Elements")
    st.write("Manages Sections of Page")


# Empty Placeholders
