"""
🛠️ Chapter 11 Workshop – Streamlit App Auth Integration

Objective:
Add full Supabase authentication to a Streamlit app:
- Register / Login page
- Store user profiles
- Show user role
- Logout and session handling

✅ Instructions:
- Integrate with existing Streamlit project (main_app.py)
- Replace placeholders and TODOs
"""

import streamlit as st
from supabase import create_client, Client

SUPABASE_URL = "https://kyanyydvgfdjsirsjmvr.supabase.co"
SUPABASE_KEY = "<YOUR_SUPABASE_KEY>"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def register_user(email, password):
    try:
        response = supabase.auth.sign_up({"email": email, "password": password})
        user = response.user
        if user:
            supabase.table("profiles").insert({"id": user.id, "email": email, "role": "user"}).execute()
        return True, "Registration successful!"
    except Exception as e:
        return False, str(e)

def login_user(email, password):
    try:
        response = supabase.auth.sign_in_with_password({"email": email, "password": password})
        return response
    except Exception as e:
        return None

def get_user_role(user_id):
    try:
        data = supabase.table("profiles").select("role").eq("id", user_id).single().execute()
        return data.data.get("role", "user")
    except:
        return "user"

# Streamlit App
st.set_page_config(page_title="🔐 Chapter 11: Supabase Auth")
st.title("🔐 Supabase Authentication")

if "user" not in st.session_state:
    st.session_state.user = None
if "user_role" not in st.session_state:
    st.session_state.user_role = None

if not st.session_state.user:
    choice = st.radio("Choose:", ["Login", "Register"])
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if choice == "Login":
        if st.button("Login"):
            result = login_user(email, password)
            if result:
                st.session_state.user = result.user
                st.session_state.user_role = get_user_role(result.user.id)
                st.success("Login successful!")
                st.experimental_rerun()
            else:
                st.error("Invalid credentials.")
    else:
        if st.button("Register"):
            success, msg = register_user(email, password)
            st.success(msg) if success else st.error(msg)

    st.stop()

st.success(f"🎉 Welcome {st.session_state.user.email}, Role: {st.session_state.user_role}")
if st.button("Logout"):
    supabase.auth.sign_out()
    st.session_state.user = None
    st.session_state.user_role = None
    st.experimental_rerun()
