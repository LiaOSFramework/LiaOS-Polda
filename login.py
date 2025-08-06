import streamlit as st

def login():
    st.title("Login LiaOS – Polda")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state["role"] = "admin"
            st.session_state["logged_in"] = True
            st.experimental_rerun()
        elif username == "humas" and password == "1234":
            st.session_state["role"] = "user"
            st.session_state["logged_in"] = True
            st.experimental_rerun()
        else:
            st.error("Username atau password salah")
