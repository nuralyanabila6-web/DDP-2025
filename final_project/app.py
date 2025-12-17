import streamlit as st

st.set_page_config(page_title="Beressin", page_icon="📝")

st.title("📝 Selamat Datang di Aplikasi Beressin!")
st.write("Aplikasi To-Do List sederhana untuk Final Project Dasar-Dasar Pemrograman.")

st.image("icon.png", width=150)

st.markdown("""
### Menu Navigasi:
Gunakan menu *di sebelah kiri (sidebar)* untuk berpindah halaman:
- 📄 Lihat Tugas
- ➕ Tambah Tugas
- ❌ Hapus Tugas
- ℹ️ Tentang Aplikasi
""")

# Inisialisasi session state
if "list_tugas" not in st.session_state:

    st.session_state.list_tugas = []

