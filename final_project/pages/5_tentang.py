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



def about_developer():
    st.header("👨‍💻 Tentang Pengembang")
    st.markdown("""
    **Nama:** John Doe  
    **NIM:** 123456789  
    **Program Studi:** Teknik Informatika  
    **Universitas:** Universitas Contoh  
    """)