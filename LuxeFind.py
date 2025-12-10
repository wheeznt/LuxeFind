# Program Login, Register, dan Request Barang
# Versi sangat sederhana untuk mahasiswa semester 1

users = {}          # menyimpan email dan password
requests = []       # menyimpan permintaan barang


def register():
    print("\n=== REGISTER ===")
    email = input("Masukkan email: ")
    password = input("Masukkan password: ")

    if email in users:
        print("Email sudah terdaftar!\n")
    else:
        users[email] = password
        print("Registrasi berhasil!\n")


def login():
    print("\n=== LOGIN ===")
    email = input("Masukkan email: ")
    password = input("Masukkan password: ")

    if email in users and users[email] == password:
        print("Login berhasil! Selamat datang,", email, "\n")
        menu_user(email)   # masuk ke menu setelah login
    else:
        print("Email atau password salah!\n")


# ===============================
# FITUR BARU: PERMINTAAN BARANG
# ===============================
def buat_request(email):
    print("\n=== BUAT PERMINTAAN BARANG ===")
    barang = input("Nama barang: ")
    deskripsi = input("Deskripsi barang: ")

    req = {
        "email": email,
        "barang": barang,
        "deskripsi": deskripsi
    }

    requests.append(req)
    print("Permintaan berhasil dibuat!\n")


def lihat_request(email):
    print("\n=== DAFTAR PERMINTAAN ANDA ===")

    ada_data = False
    for r in requests:
        if r["email"] == email:
            print(f"- {r['barang']} : {r['deskripsi']}")
            ada_data = True

    if not ada_data:
        print("Belum ada permintaan barang.\n")


# ===============================
# MENU SETELAH LOGIN
# ===============================
def menu_user(email):
    while True:
        print("=== MENU USER ===")
        print("1. Buat permintaan barang")
        print("2. Lihat permintaan saya")
        print("3. Logout")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            buat_request(email)
        elif pilihan == "2":
            lihat_request(email)
        elif pilihan == "3":
            print("Logout berhasil!\n")
            break
        else:
            print("Pilihan tidak valid!\n")


# ===============================
# MENU UTAMA
# ===============================
def main():
    while True:
        print("=== LUXEFIND CLI ===")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            login()
        elif pilih == "2":
            register()
        elif pilih == "3":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!\n")


main()
