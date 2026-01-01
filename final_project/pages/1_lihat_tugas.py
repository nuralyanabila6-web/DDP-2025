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

            #update

#Catatan
st.subheader("Catatan:")
st.info("Catatan yang terakhir ditambahkan akan muncul jika anda memasukan catatan baru agar ingatan anda semakin tajam")
if "catatan" not in st.session_state:
    st.session_state.catatan = []

def add_catatan():
    catatan_baru = st.text_input("Masukkan catatan baru:")
    if st.button("Tambah Catatan"):
        if catatan_baru:
            st.session_state.catatan.append(catatan_baru)
            st.success("Catatan berhasil ditambahkan!")

if st.session_state.catatan:
    st.write("Daftar Catatan:")
    for idx, catatan in enumerate(st.session_state.catatan, 1):
        st.write(f"{idx}. {catatan}")

def remove_catatan():
    if st.session_state.catatan:
        catatan_hapus = st.selectbox("Pilih catatan untuk dihapus:", st.session_state.catatan)
        if st.button("Hapus Catatan"):
            st.session_state.catatan.remove(catatan_hapus)
            st.success("Catatan berhasil dihapus!") 

add_catatan()
remove_catatan()
