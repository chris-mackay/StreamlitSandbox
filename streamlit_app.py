import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = [
        "Laugh out loud",
        "Get the popcorn",
        "Never stop learning"
    ]
)

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy")
else:
    st.write("You didn't select comedy")


@st.cache_data
def get_data():
    df = pd.DataFrame(
        np.random.randn(50, 20), columns=("col %d" % i for i in range(20))
    )
    return df

@st.cache_data
def convert_for_download(df):
    return df.to_csv().encode("utf-8")

df = get_data()
csv = convert_for_download(df)

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="data.csv",
    mime="text/csv",
    icon=":material/download:",
)

number = st.number_input("Insert a number")
st.write("The current number is ", number)

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    string_data = stringio.read()

    st.write(string_data)

    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

uploaded_files = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=True
)

for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)