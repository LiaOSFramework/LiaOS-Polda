import streamlit as st

def show():
    st.markdown("## 🔍 Scan Narasi")
    st.write("Masukkan kata kunci atau link untuk memindai narasi publik.")
    st.divider()
    keyword = st.text_input("Kata kunci / URL")
    if st.button("🔍 Pindai"):
        st.warning("⏳ Sedang memindai... (fitur demo)")
