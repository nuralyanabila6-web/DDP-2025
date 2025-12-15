import streamlit as st

st.title("❌ Hapus Tugas")

if "list_tugas" not in st.session_state:
    st.session_state.list_tugas = []

if len(st.session_state.list_tugas) == 0:
    st.info("Tidak ada tugas untuk dihapus.")
else:
    nomor_hapus = st.number_input("Masukkan nomor tugas:", min_value=1, max_value=len(st.session_state.list_tugas))

    if st.button("Hapus"):
        index = nomor_hapus - 1
        tugas = st.session_state.list_tugas.pop(index)
        # Jika tugas adalah dict, gunakan nama tugas untuk pesan
        nama_tugas = tugas.get("nama") if isinstance(tugas, dict) else tugas
        st.success(f"Tugas '{nama_tugas}' berhasil dihapus!")