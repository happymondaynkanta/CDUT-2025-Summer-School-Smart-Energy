#!/usr/bin/env python
# coding: utf-8

# # 🎓 Chapter 8: Building the Prediction Page UI

# This workshop will guide you through building a user-friendly prediction interface with input validation, output metrics, and modular layout using Streamlit.

# ## 1. Setup

# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np
import joblib


# ## 2. UI Layout – Page Title and Form

# In[ ]:


st.title("Energy Forecast Dashboard")
with st.form("prediction_form"):
    hour = st.slider("Hour of Day", 0, 23, 12)
    temperature = st.number_input("Temperature (°C)", min_value=-10.0, max_value=50.0, value=25.0)
    submitted = st.form_submit_button("Predict")


# ## 3. Load Model & Validate Inputs

# In[ ]:


if submitted:
    if temperature < -5 or temperature > 45:
        st.warning("⚠️ Unusual temperature entered!")
    model = joblib.load("models/xgb_energy_model.pkl")
    features = np.array([[hour, temperature]])
    prediction = model.predict(features)[0]


# ## 4. Display Output using st.metric

# In[ ]:


st.metric("Predicted Load (kW)", f"{prediction:.2f}")


# ## 5. Optional Logging

# In[ ]:


with open("logs/predictions_log.csv", "a") as f:
    f.write(f"{hour},{temperature},{prediction:.2f}\n")


# ## 6. Final Layout Suggestions

# In[ ]:


st.markdown("<h4 style='color:green'>Thank you for using the dashboard!</h4>", unsafe_allow_html=True)

