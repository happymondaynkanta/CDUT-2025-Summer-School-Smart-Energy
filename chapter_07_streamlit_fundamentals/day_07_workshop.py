#!/usr/bin/env python
# coding: utf-8

# # 🎓 Chapter 7: Streamlit Fundamentals

# This workshop introduces Streamlit for creating interactive dashboards using real-world energy data.

# ## 1. Install Streamlit

# In[ ]:


get_ipython().system('pip install streamlit')


# ## 2. First Run

# In[ ]:


get_ipython().system('streamlit run app.py  # run this from terminal')


# ## 3. Widgets Overview

# In[ ]:


import streamlit as st

st.title("Energy Dashboard")
st.slider("Threshold", 0, 100, 25)
st.text_input("Building Name")
st.button("Predict")


# ## 4. Sidebar Filters

# In[ ]:


with st.sidebar:
    st.header("Filters")
    st.slider("Energy Limit", 0, 500, 200)


# ## 5. Layout and Expander

# In[ ]:


col1, col2 = st.columns(2)
col1.metric("Predicted Usage", "500 kWh")
with st.expander("See Explanation"):
    st.write("Details about prediction")


# ## 6. Styling with Markdown and Plot

# In[ ]:


st.markdown("<h3 style='color:blue'>Energy Trends</h3>", unsafe_allow_html=True)
st.line_chart([10, 20, 15, 30, 40])

