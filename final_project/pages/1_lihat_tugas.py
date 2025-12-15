import streamlit as st

st.title("📄 Lihat Daftar Tugas")

if "list_tugas" not in st.session_state:
    st.session_state.list_tugas = []

if len(st.session_state.list_tugas) == 0:
    st.info("Daftar tugas masih kosong.")
else:
    for i, tugas in enumerate(st.session_state.list_tugas, 1):
        # Tugas bisa disimpan sebagai dict (dengan kunci 'nama' dan 'selesai')
        if isinstance(tugas, dict):
            status = "✅ SELESAI" if tugas.get("selesai") else "❌ BELUM"
            st.write(f"{i}. {tugas.get('nama')} - {status}")
        else:
            # Backward compatibility jika tugas masih string
            st.write(f"{i}. {tugas}")