import pandas as pd
import numpy as np
import matplotlib as plt
import streamlit as st

st.title("Charts Demo")

data_set = np.random.randint(20, 60, 60).reshape(20, 3)
chart_data = pd.DataFrame(
    data_set,  # 20 rows, 3 columns
    columns=["Male", "Female", "Unknown"],
    index=range(1, len(data_set) + 1)
)
chart_data

# Area Chart Section
st.subheader("Area Chart")
st.area_chart(chart_data)

#Bar Chart Section
st.subheader("Bar Chart")
st.bar_chart(chart_data)