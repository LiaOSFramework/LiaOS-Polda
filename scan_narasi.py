import streamlit as st

def show():
    st.header("Scan Narasi")
    narasi = st.text_area("Masukkan narasi yang akan dianalisis")
    if st.button("Analisis Sekarang (AI)"):
        # Dummy result - ganti nanti dengan fungsi AI LiaOS
        st.write("**Bias**: Ada framing 'viral' yang bisa mempengaruhi persepsi publik")
        st.write("**Fallacy**: Generalisasi berlebihan tanpa bukti")
        st.write("**Emosi**: Nada marah dan sinis")
        st.write("**Reframing**: Arahkan fokus ke verifikasi fakta dan konteks")
