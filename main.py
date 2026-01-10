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

    #fetch unique users
    user_list =df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Overall Group")

    st.sidebar.selectbox("Show analysis for ",user_list)