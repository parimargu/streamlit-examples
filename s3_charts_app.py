import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['Java', 'Ruby', 'Python'])

st.dataframe(chart_data)


st.line_chart(chart_data)