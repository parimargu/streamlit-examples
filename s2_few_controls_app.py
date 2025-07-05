import streamlit as st

llm_list = ["GPT-3.5", "GPT-4", "Claude 2", "Claude 3", "Gemini Pro"]

st.title("Streamlit App 2")

selected_llm = st.radio("Select LLM", llm_list)

if selected_llm == "GPT-3.5":
    st.write("You selected GPT-3.5")
elif selected_llm == "GPT-4":
    st.write("You selected GPT-4")

selected_llm = st.radio("Select LLM", llm_list, horizontal=True)

if selected_llm == "GPT-3.5":
    st.write("You selected GPT-3.5")
elif selected_llm == "GPT-4":
    st.write("You selected GPT-4")


selected_city = st.selectbox("Select City", ["New York", "Los Angeles", "Chicago"])
if selected_city == "New York":
    st.write("You selected New York")
elif selected_city == "Los Angeles":
    st.write("You selected Los Angeles")
elif selected_city == "Chicago":
    st.write("You selected Chicago")

selected_city = st.selectbox("Select City", ["New York", "Los Angeles", "Chicago"], index=1)
if selected_city == "New York":
    st.write("You selected New York")
elif selected_city == "Los Angeles":
    st.write("You selected Los Angeles")
elif selected_city == "Chicago":
    st.write("You selected Chicago")

