# import streamlit as st

# st.write("Single Page Application.")     # Magic command, we can write anything, the same gets displayed in the UI with the same Data Type
# st.write({
#     "name": "ABS",
#     "ID": "111"
# })


# "Present" if True else "Absent"

# # DataFlow
# print("Running...") # Proves that whole Script reruns again & again

# btn = st.button("Pressed")
# print(btn)

# States in Streamlit

import pandas as pd
import streamlit as st
import os

st.title("Dashboard")
st.header("Data Dashboard")
# st.subheader("Data Dashboard")
# st.markdown("Data")
# st.caption("Data")

st.divider()

# get the current working directory
st.image(os.path.join(os.getcwd(), "static", "bg.jpg"))

st.divider()

# Data Elelents
df = pd.DataFrame({
    "Name": ["ABS", "ALI", "AVI", "JOY", "ROY", "JOE", "DOI"],
    "Age": [23, 45, 67, 83, 23, 34, 54],
    "Designation": ["SDE1", "SDE2", "SDE3", "SDE2", "OPS", "MNGT", "OPS"]
})
st.dataframe(df)    # editable dataframe, liek sorting, downloading etc

# Data Editor Section(Editable Dataframe)
st.subheader("Data Editor")
editable_df = st.data_editor(df)
print(editable_df)

# Static Table Section is used for no interaction, like sorting, downloading etc.
st.subheader("Static Table")
st.table(df)


# Metrics Section
st.subheader("Data Metrics")
st.metric(label="Total", value=len(df))
st.metric(label="Mean", value=df['Age'].mean())

# converting DF into json
st.json(df.to_json())
