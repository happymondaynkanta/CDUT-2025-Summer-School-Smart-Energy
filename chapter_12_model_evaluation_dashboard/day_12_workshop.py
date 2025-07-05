
# day_12_workshop.py
# Author: Dr. Grace Ugochi Nneji, Dr. Happy Nkanta Monday
# Workshop: Data Upload and Persistence with Supabase and Streamlit

import streamlit as st
from supabase import create_client
import os
from datetime import datetime
import pandas as pd

# Supabase credentials
SUPABASE_URL = "https://kyanyydvgfdjsirsjmvr.supabase.co"
SUPABASE_KEY = "your_supabase_key_here"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Bucket for file uploads
UPLOAD_BUCKET = "uploads"

st.title("📤 Data Upload & Persistence Workshop")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    file_bytes = uploaded_file.getvalue()
    file_name = uploaded_file.name

    # Upload file to Supabase Storage
    supabase.storage.from_(UPLOAD_BUCKET).upload(file_name, file_bytes)

    # Log upload in the database
    result = supabase.table("prediction_logs").insert({
        "filename": file_name,
        "timestamp": datetime.utcnow().isoformat(),
        "email": "test_user@example.com",  # Replace with real session-based user
        "prediction": "Uploaded file"
    }).execute()

    st.success("✅ File uploaded and logged successfully!")

# View file history
st.subheader("📂 Uploaded File History")

history = supabase.table("prediction_logs").select("*").order("timestamp", desc=True).execute()
df = pd.DataFrame(history.data)
if not df.empty:
    st.dataframe(df)
else:
    st.info("No file logs yet.")
