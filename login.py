import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

USERNAME = os.getenv("LIAOS_USER")
PASSWORD = os.getenv("LIAOS_PASS")

def login():
    st.title("Login LiaOS – Polda")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state["logged_in"] = True
            st.session_state["role"] = "Admin"
            st.success("✅ Login berhasil! Silakan pilih menu di sidebar.")
        else:
            st.error("❌ Username atau password salah.")
