import streamlit as st
import pandas as pd

st.header("File Uploader App")
st.title("Upload your files here")

uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt", "xlsx"])

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write("File uploaded successfully!")
    
    # Display the file content
    if uploaded_file.type == "text/csv":

        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
    elif uploaded_file.type == "text/plain":
        text_data = bytes_data.decode("utf-8")
        st.text(text_data)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":

        df = pd.read_excel(uploaded_file)
        st.dataframe(df)
        