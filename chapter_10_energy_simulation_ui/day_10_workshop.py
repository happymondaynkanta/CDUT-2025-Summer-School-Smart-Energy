# --- Markdown Cell ---
# # 🔐 Chapter 10: Supabase Authentication & Authorization
# **Workshop Notebook**
# 
# Learn how to integrate Supabase into your Python and Streamlit apps. This workshop walks through:
# - Creating a Supabase project
# - Register/Login flow
# - Role-based access control
# - Storing user profiles securely
# - Real-time data with RLS (Row Level Security)
# --- Code Cell ---
# ✅ Setup Supabase Client
from supabase import create_client, Client
SUPABASE_URL = 'https://your-project.supabase.co'
SUPABASE_KEY = 'your-anon-or-service-role-key'
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
# --- Code Cell ---
# 👤 Register a New User
def register_user(email, password):
    response = supabase.auth.sign_up({'email': email, 'password': password})
    return response
# --- Code Cell ---
# 🔑 Login Existing User
def login_user(email, password):
    response = supabase.auth.sign_in_with_password({'email': email, 'password': password})
    return response.session, response.user
# --- Markdown Cell ---
# ## ✅ TASK: Connect and Test
# 1. Create a Supabase project.
# 2. Create a table called `profiles` with fields: `id`, `email`, `role`.
# 3. Try registering and logging in users.
# 4. Print out the session token and user email.
