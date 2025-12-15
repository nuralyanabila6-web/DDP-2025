import streamlit as st

st.title("📄 Lihat Daftar Tugas")

if "list_tugas" not in st.session_state:
    st.session_state.list_tugas = []

if len(st.session_state.list_tugas) == 0:
    st.info("Daftar tugas masih kosong.")
else:
    for i, tugas in enumerate(st.session_state.list_tugas, 1):
        st.write(f"{i}. {tugas}")

        #asdas