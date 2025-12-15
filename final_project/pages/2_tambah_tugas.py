import streamlit as st

st.title("➕ Tambah Tugas Baru")

if "list_tugas" not in st.session_state:
    st.session_state.list_tugas = []

tugas_baru = st.text_input("Masukkan nama tugas:")

# if st.button("Tambah"):
#     if tugas_baru.strip():
#         st.session_state.list_tugas.append(tugas_baru.strip())
#         st.success(f"Tugas '{tugas_baru}' berhasil ditambahkan!")
#     else:
#         st.error("Input tidak boleh kosong.")
if st.button("Tambah"):
    if tugas_baru.strip():
        st.session_state.list_tugas.append({
            "nama tugas": tugas_baru.strip(),
            "selesai": False
        })
        st.success("Tugas berhasil ditambahkan!")
    else:
        st.error("Input tidak boleh kosong.")