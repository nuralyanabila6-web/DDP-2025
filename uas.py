# Final Project Dasar-Dasar Pemrograman: Aplikasi "Beressin" (To-Do List Sederhana)

# 1. Inisialisasi List Tugas (List/Array)
list_tugas = []

# --- 2. Modul Lihat Tugas (Fungsi) ---
def lihat_tugas():
    """Menampilkan semua tugas yang ada dalam list_tugas."""
    print("\n--- Daftar Tugas Beressin ---")
    
    # Percabangan: Cek apakah list kosong
    if not list_tugas:
        print("ℹ️ Daftar tugas kosong. Mari tambah tugas baru!")
    else:
        # Perulangan: Menggunakan enumerate untuk menampilkan nomor urut yang benar
        # (dimulai dari 1, bukan 0)
        for index, tugas in enumerate(list_tugas, 1):
            print(f"{index}. {tugas}")
            
    print("-----------------------------")

# --- 3. Modul Tambah Tugas (Fungsi) ---
def tambah_tugas():
    """Meminta input dan menambahkan tugas baru ke dalam list."""
    tugas_baru = input("Masukkan nama tugas baru: ")
    
    # Validasi: Pastikan input tidak hanya spasi kosong
    if tugas_baru.strip():
        list_tugas.append(tugas_baru.strip())
        print(f"✅ Tugas '{tugas_baru.strip()}' berhasil ditambahkan!")
    else:
        print("❌ Tugas tidak boleh kosong.")

# --- 4. Modul Hapus Tugas & Validasi (Fungsi) ---
def hapus_tugas():
    """Menghapus tugas berdasarkan nomor urut dengan validasi."""
    
    # Cek dulu apakah ada yang bisa dihapus
    if not list_tugas:
        print("ℹ️ Tidak ada tugas untuk dihapus. Daftar kosong.")
        return # Keluar dari fungsi jika list kosong

    # Tampilkan list agar pengguna tahu nomornya
    lihat_tugas() 
    
    try:
        # Minta input nomor, lalu konversi ke integer
        nomor_input = input("Masukkan NOMOR tugas yang ingin dihapus: ")
        nomor_hapus = int(nomor_input)
        
        # Validasi Rentang (sesuai flowchart)
        # Indeks List dimulai dari 0, jadi nomor_hapus dikurangi 1
        indeks_hapus = nomor_hapus - 1
        
        # Percabangan: Cek apakah indeks berada dalam rentang yang valid
        if 0 <= indeks_hapus < len(list_tugas):
            # Proses: Hapus tugas menggunakan pop()
            tugas_dihapus = list_tugas.pop(indeks_hapus)
            print(f"🗑️ Tugas nomor {nomor_hapus} ('{tugas_dihapus}') berhasil dihapus!")
        else:
            print(f"❌ ERROR: Nomor {nomor_hapus} tidak valid atau tidak ditemukan.")
            
    except ValueError:
        # Penanganan error jika input bukan angka
        print("❌ ERROR: Input harus berupa angka.")
    except Exception as e:
        # Penanganan error umum
        print(f"❌ Terjadi error: {e}")

# --- 5. Main Program & Menu Loop (Modul 1) ---
def tampilkan_menu():
    """Menampilkan opsi menu utama."""
    print("\n=== Aplikasi Beressin ===")
    print("1. Lihat Daftar Tugas")
    print("2. Tambah Tugas Baru")
    print("3. Hapus Tugas")
    print("4. Keluar dari Aplikasi")
    print("=========================")

def main_beressin():
    # Perulangan Utama (While True)
    while True:
        tampilkan_menu()
        
        # Input Pilihan
        pilihan = input("Masukkan pilihan Anda (1-4): ")
        
        # Percabangan Utama (If/Elif/Else)
        if pilihan == '1':
            lihat_tugas()
            
        elif pilihan == '2':
            tambah_tugas()
            
        elif pilihan == '3':
            hapus_tugas()
            
        elif pilihan == '4':
            # Logika Keluar
            print("\nTerima kasih telah menggunakan Aplikasi Beressin. Sampai jumpa!")
            break # Perintah untuk keluar dari perulangan
            
        else:
            # Penanganan input menu tidak valid
            print("ERROR: Pilihan tidak valid. Silakan masukkan angka antara 1 sampai 4.")
        
# Memanggil fungsi utama agar program berjalan
if _name_ == "_main_":
    main_beressin()
