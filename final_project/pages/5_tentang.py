import streamlit as st

st.title("ℹ️ Tentang Aplikasi")

st.markdown("""
Aplikasi *Beressin* adalah aplikasi Task Manajer untuk mengelola tugas harian. Aplikasi ini dapat membantu user mengatur tugas agar tetap teratur.

Fitur:
- Melihat daftar tugas
- Menambah tugas
- Menghapus tugas
- Navigasi mudah antar halaman

""")

def tentang_developer():
    st.subheader("Tentang Developer")
    st.markdown("""
    Aplikasi ini dikembangkan oleh:
    - Kelompok: 17 DDP
    - anggota:
        - Adi Ardiansah (0110120119)
        - Ahmad Fathi Ahlul Rayan (0110125020)
        - Nur Alya Nabila (0110125035)
        - Revana Putri Cahya Rani (0110125092)
    """)
tentang_developer()