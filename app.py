import streamlit as st
from login import login
from pages import beranda, scan_narasi, riwayat_analisis, rekomendasi_respon, feed_narasi, export_ke_wa, pengaturan

st.set_page_config(page_title="LiaOS – Polda", layout="wide")

# Init session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "role" not in st.session_state:
    st.session_state["role"] = None

# Login page
if not st.session_state["logged_in"]:
    login()

else:
    # Sidebar
    st.sidebar.image("assets/logo_polda.png", width=100)
    st.sidebar.title("LiaOS – Polda")
    st.sidebar.markdown(f"**Role:** {st.session_state['role'].capitalize()}")
    menu = st.sidebar.radio(
        "Navigasi", 
        ["Beranda", "Scan Narasi", "Riwayat Analisis", "Rekomendasi Respon", "Feed Narasi Viral", "Export/Kirim ke WA", "Pengaturan"]
    )

    # Routing
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
