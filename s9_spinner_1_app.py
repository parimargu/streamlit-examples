import streamlit as st
import time

st.write("This is a simple spinner app.")

with st.spinner("Wait for it..."):
    time.sleep(1)

    for i in range(50):
        time.sleep(5)
        st.write(f"Step {i + 1} completed.")

st.success("Done!")

st.button("Rerun")