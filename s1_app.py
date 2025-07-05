import streamlit as st

st.title("Streamlit App 1")
st.write("This is the first Streamlit app in the multi-app setup.")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}! Welcome to the first app.")

age = st.number_input("Enter your age:", min_value=0, max_value=100, value=25)
st.write(f"You are {age} years old.")

btn = st.button("Click me to see a message")
print("Button clicked:", btn)
print(dir(btn))
if btn:
    st.write("Button clicked!")