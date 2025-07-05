import streamlit as st

import requests

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

if add_slider:
    st.sidebar.write(f'Selected range: {add_slider}')

if st.sidebar.button('Click me'):
    st.sidebar.write('Button clicked!')
