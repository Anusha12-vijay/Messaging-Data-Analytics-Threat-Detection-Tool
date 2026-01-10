import streamlit as st
import re
import preprocessor
st.sidebar.title("Messaging Data Analytics & Threat Detection Tool")

uploaded_file =st.sidebar.file_uploader("Choose the chat file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    # st.text(data)
    df=preprocessor.preprocess(data)

    st.dataframe(df)