import streamlit as st

def show():
    st.header("Export/Kirim ke WA")
    st.write("📤 Fitur ini akan mengirimkan ringkasan analisis ke nomor WhatsApp yang ditentukan.")
    nomor = st.text_input("Masukkan nomor WA (format: +62...)")
    if st.button("Kirim"):
        st.success(f"Laporan terkirim ke {nomor
