import streamlit as st

def login():
    st.header("Login LiaOS – Polda")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == "polda" and password == "liaos123":
            st.session_state["logged_in"] = True
            st.session_state["role"] = "admin"
            st.success("Login berhasil")
        else:
            st.error("❌ Username atau password salah.")
