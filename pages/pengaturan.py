import streamlit as st

def show():
    st.markdown("## ⚙️ Pengaturan")
    st.write("Atur preferensi aplikasi LiaOS – Polda.")
    st.divider()
    st.text_input("Ganti username")
    st.text_input("Ganti password", type="password")
    if st.button("💾 Simpan"):
        st.success("✅ Pengaturan berhasil disimpan (simulasi).")
