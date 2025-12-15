import streamlit as st

st.title("✅ Tandai Tugas Selesai")

# Inisialisasi list tugas jika belum ada
if "list_tugas" not in st.session_state:
    st.session_state.list_tugas = []

# ================= FUNCTION =================
def tandai_selesai(index):
    """Menandai tugas sebagai selesai berdasarkan index"""
    st.session_state.list_tugas[index]["selesai"] = True
# ============================================

if len(st.session_state.list_tugas) == 0:
    st.info("Tidak ada tugas untuk ditandai.")
else:
    for i, tugas in enumerate(st.session_state.list_tugas):
        status = "✅ SELESAI" if tugas["selesai"] else "❌ BELUM"
        st.write(f"{i+1}. {tugas['nama']} - {status}")

    nomor = st.number_input(
        "Masukkan nomor tugas yang sudah selesai:",
        min_value=1,
        max_value=len(st.session_state.list_tugas),
        step=1
    )

    if st.button("Tandai Selesai"):
        index = nomor - 1
        if not st.session_state.list_tugas[index]["selesai"]:
            tandai_selesai(index)
            st.success("Tugas berhasil ditandai sebagai selesai!")
            # Rerun agar tampilan daftar terupdate segera
            st.experimental_rerun()
        else:
            st.warning("Tugas ini sudah selesai.")