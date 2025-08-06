import streamlit as st
from fpdf import FPDF
from datetime import datetime
import openai
import os

# ===== CONFIG PAGE =====
st.set_page_config(page_title="LiaOS Polda", layout="wide", page_icon="🛡")

# ===== SET API KEY =====
openai.api_key = st.secrets.get("OPENAI_API_KEY")

# ===== CUSTOM CSS DARK THEME =====
st.markdown("""
<style>
    .main { background-color: #0E1117; color: white; }
    .stSidebar { background-color: #1E232F; }
    .stButton>button { background-color: #2E86C1; color: white; border-radius: 8px; height: 40px; }
    .risk-high { background-color: #FF4C4C; padding: 4px 8px; border-radius: 6px; color: white; }
    .risk-med { background-color: #FFA500; padding: 4px 8px; border-radius: 6px; color: white; }
    .risk-low { background-color: #4CAF50; padding: 4px 8px; border-radius: 6px; color: white; }
</style>
""", unsafe_allow_html=True)

# ===== DUMMY DATA =====
narasi_viral = [
    {"judul": "Protes Masyarakat Riau Atas Kebijakan BBM", "risiko": "Tinggi"},
    {"judul": "Video Hoaks Polisi di UIR Beredar Luas", "risiko": "Sedang"},
    {"judul": "5 Fakta Baru Tragedi Stadion Utama", "risiko": "Rendah"},
]

# ===== FUNCTION ANALISIS AI =====
def analisis_liaos_ai(narasi):
    prompt = f"""
    Lakukan analisis narasi berikut dengan kerangka LiaOS (5 layer):
    0. Intent – Deteksi niat utama narasi.
    1. Bias – Bias kognitif atau framing yang muncul.
    2. Refleksi – Makna atau dampak narasi terhadap audiens.
    3. Emosi – Emosi dominan yang dibangkitkan.
    4. Reframing – Cara membingkai ulang untuk tujuan netral/positif.

    Narasi: {narasi}
    Berikan jawaban singkat tapi jelas untuk tiap layer.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Kamu adalah analis narasi untuk LiaOS Polda."},
                  {"role": "user", "content": prompt}],
        max_tokens=500
    )
    hasil_text = response.choices[0].message["content"].strip()
    
    # Parsing hasil jadi dict layer
    hasil_dict = {}
    for line in hasil_text.split("\n"):
        if "-" in line:
            parts = line.split("-", 1)
            if len(parts) == 2:
                layer = parts[0].strip()
                analisis = parts[1].strip()
                hasil_dict[layer] = analisis
    return hasil_dict

# ===== FUNCTION EXPORT PDF =====
def export_pdf(narasi, hasil):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Laporan Analisis LiaOS Polda", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, f"Tanggal: {datetime.now().strftime('%d-%m-%Y %H:%M')}", ln=True)
    pdf.ln(5)
    pdf.multi_cell(0, 10, f"NARASI:\n{narasi}\n")
    for layer, analisis in hasil.items():
        pdf.multi_cell(0, 10, f"{layer}:\n{analisis}\n")
    return pdf.output(dest='S').encode('latin-1')

# ===== SIDEBAR =====
menu = st.sidebar.radio("Navigasi", ["Beranda", "Scan Narasi", "Riwayat Analisis", "Export PDF", "Pengaturan"])

# ===== HALAMAN BERANDA =====
if menu == "Beranda":
    st.title("📊 LiaOS - Dashboard Polda")
    st.subheader("Highlight Hari Ini")
    for item in narasi_viral:
        risk_class = "risk-high" if item['risiko']=="Tinggi" else "risk-med" if item['risiko']=="Sedang" else "risk-low"
        st.markdown(f"<div class='{risk_class}'>{item['risiko']}</div> {item['judul']}", unsafe_allow_html=True)

# ===== SCAN NARASI =====
elif menu == "Scan Narasi":
    st.title("🔍 Scan Narasi")
    narasi_input = st.text_area("Masukkan narasi yang akan dianalisis")
    if st.button("Analisis Sekarang (AI)"):
        if narasi_input.strip():
            with st.spinner("Menganalisis dengan AI..."):
                hasil = analisis_liaos_ai(narasi_input)
            for layer, analisis in hasil.items():
                st.markdown(f"**{layer}**: {analisis}")
            st.session_state['last_analysis'] = (narasi_input, hasil)
        else:
            st.warning("Masukkan narasi terlebih dahulu.")

# ===== RIWAYAT ANALISIS =====
elif menu == "Riwayat Analisis":
    st.title("🗂 Riwayat Analisis")
    if 'last_analysis' in st.session_state:
        narasi, hasil = st.session_state['last_analysis']
        st.write(f"**Narasi:** {narasi}")
        for layer, analisis in hasil.items():
            st.write(f"**{layer}**: {analisis}")
    else:
        st.info("Belum ada analisis yang disimpan.")

# ===== EXPORT PDF =====
elif menu == "Export PDF":
    st.title("📄 Export Hasil Analisis ke PDF")
    if 'last_analysis' in st.session_state:
        narasi, hasil = st.session_state['last_analysis']
        if st.button("Download PDF"):
            pdf_data = export_pdf(narasi, hasil)
            st.download_button("💾 Simpan PDF", pdf_data, file_name="Laporan_LiaOS.pdf", mime="application/pdf")
    else:
        st.warning("Belum ada analisis untuk diexport.")

# ===== PENGATURAN =====
elif menu == "Pengaturan":
    st.title("⚙️ Pengaturan")
    st.write("Pastikan API Key OpenAI sudah diisi di menu Secrets Streamlit untuk mengaktifkan analisis AI.")
