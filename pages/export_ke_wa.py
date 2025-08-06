import streamlit as st

def show():
    st.markdown("## 📤 Export / Kirim ke WA")
    st.write("Kirim laporan hasil analisis ke WhatsApp.")
    st.divider()
    nomor = st.text_input("Nomor WhatsApp (format: +62...)")
    if st.button("📤 Kirim"):
        st.success(f"✅ Laporan berhasil dikirim ke {nomor} (simulasi).")
