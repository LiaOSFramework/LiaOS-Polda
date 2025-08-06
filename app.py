import streamlit as st
from login import login
from pages import beranda
from pages import scan_narasi
from pages import riwayat_analisis
from pages import rekomendasi_respon
from pages import feed_narasi
from pages import export_ke_wa
from pages import pengaturan
import os

st.set_page_config(page_title="LiaOS – Polda", layout="wide")

# Load CSS jika ada
if os.path.exists("styles.css"):
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Init Session State
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "role" not in st.session_state:
    st.session_state["role"] = None

# Login / Dashboard
if not st.session_state["logged_in"]:
    login()
else:
    # Sidebar
    logo_path = "assets/logo_polda.png"
    if os.path.exists(logo_path):
        st.sidebar.image(logo_path, width=100)
    else:
        st.sidebar.markdown("**[Logo belum diupload]**")

    st.sidebar.title("LiaOS – Polda")
    st.sidebar.markdown(f"**Role:** {st.session_state['role'].capitalize()}")

    menu = st.sidebar.radio(
        "Navigasi",
        [
            "Beranda",
            "Scan Narasi",
            "Riwayat Analisis",
            "Rekomendasi Respon",
            "Feed Narasi Viral",
            "Export/Kirim ke WA",
            "Pengaturan"
        ]
    )

    # Routing Halaman
    if menu == "Beranda":
        beranda.show()
    elif menu == "Scan Narasi":
        scan_narasi.show()
    elif menu == "Riwayat Analisis":
        riwayat_analisis.show()
    elif menu == "Rekomendasi Respon":
        rekomendasi_respon.show()
    elif menu == "Feed Narasi Viral":
        feed_narasi.show()
    elif menu == "Export/Kirim ke WA":
        export_ke_wa.show()
    elif menu == "Pengaturan":
        pengaturan.show()
