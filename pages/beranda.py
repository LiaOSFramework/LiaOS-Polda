import streamlit as st

def show():
    st.header("Highlight Hari Ini")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Protes Mahasiswa Tolak Kenaikan BBM** — 🟥 Risiko Tinggi")
        st.markdown("**Viral Polisi Arogan saat Razia** — 🟧 Risiko Sedang")
        st.markdown("**5 Fakta Terkini Kasus Subang** — 🟦 Risiko Rendah")
    
    with col2:
        st.subheader("Update Crawler Terbaru")
        st.markdown("🚔 Polisi Periksa Margiono soal Mafia Tanah — 6 min lalu")
        st.markdown("🚨 Kronologi Kecelakaan Truk di Tol Cipali — 24 min lalu")
        st.markdown("📢 Demo Tolak Proyek Reklamasi di Ancol — 1 jam lalu")

    st.subheader("Simulasi Dampak")
    narasi = st.text_input("Masukkan narasi untuk simulasi")
    if narasi:
        st.write("**Bias**: Identifikasi stereotip tentang aparat")
        st.write("**Fallacy**: Kritik tanpa menawarkan solusi konkret")
        st.write("**Emosi**: Kemarahan terhadap penyalahgunaan")
        st.write("**Reframing**: Jelaskan tujuan razia dalam penegakan hukum")
