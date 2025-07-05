import streamlit as st
import time

st.write("This is a simple spinner app.")

name_input = st.text_input("Enter your name:", key="name_input")
greet_button = st.button("Send Greetings!")

# If the button is clicked, greet the user
if greet_button:
    st.title(f"Happy birthday! {name_input}!")
    for i in range(10):
        time.sleep(0.5)  # Simulate a delay
        st.balloons()