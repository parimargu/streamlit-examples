import streamlit as st

st.sidebar.title("Side Menu Example")
st.sidebar.markdown("This is a simple sidebar menu example using Streamlit.")

# Add a few options to the sidebar
menu_options = ["Home", "About", "Contact"]
selected_option = st.sidebar.selectbox("Select an option:", menu_options)
# Display content based on the selected option
if selected_option == "Home":
    st.title("Home")
    st.write("Welcome to the home page!")
elif selected_option == "About":
    st.title("About")
    st.write("This is the about page. Here you can find information about this app.")
elif selected_option == "Contact":
    st.title("Contact")
    st.write("This is the contact page. You can reach us at [insert contact information here].")
