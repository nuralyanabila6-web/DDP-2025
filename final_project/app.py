import streamlit as st

st.set_page_config(page_title="Beressin", page_icon="📝")

st.title("📝 Selamat Datang di Aplikasi Beressin!")
st.write("Aplikasi Task Manajer sederhana.")

st.image("https://cdn-icons-png.flaticon.com/512/8297/8297557.png", width=150)

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

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi


def main():
    try:
        alas = float(input("Masukkan alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        return
    area = luas_segitiga(alas, tinggi)
    print(f"Luas segitiga: {area}")


if __name__ == "__main__":
    main()



