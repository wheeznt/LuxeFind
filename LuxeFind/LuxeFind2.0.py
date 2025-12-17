users = {}
posts = []
current_user = None

# AUTH

def register():
    email = input("Email: ")
    password = input("Password: ")
    role = input("Daftar sebagai user atau mediator: ")

    if email in users:
        print("Email sudah terdaftar")
        return

    users[email] = {
        "password": password,
        "role": role
    }
    print("Registrasi berhasil")


def login():
    global current_user
    email = input("Email: ")
    password = input("Password: ")

    if email in users and users[email]["password"] == password:
        current_user = email
        print("Login berhasil")
        beranda()
    else:
        print("Login gagal")

# USER MEMPOSTING BARANG YANG DICARI

def buat_post():
    nama = input("Nama barang yang dicari: ")
    merek = input("Merek: ")
    tahun = input("Tahun: ")
    deskripsi = input("Deskripsi tambahan: ")
    kontak = input("Kontak yang bisa dihubungi: ")

    post = {
        "user": current_user,
        "nama": nama,
        "merek": merek,
        "tahun": tahun,
        "deskripsi": deskripsi,
        "kontak": kontak
    }

    posts.append(post)
    print("Postingan berhasil ditambahkan")

# BERANDA SEPERTI E COMMERCE

def beranda():
    global current_user
    while True:
        print("\n=== BERANDA ===")

        if not posts:
            print("Belum ada permintaan barang")
        else:
            for i, p in enumerate(posts):
                print(f"{i}. {p['nama']} | {p['merek']} | {p['tahun']}")

        print("\nMenu")
        print("1 Lihat detail permintaan")

        if users[current_user]["role"] == "user":
            print("2 Buat permintaan barang")

        print("0 Kembali ke Menu Awal")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            lihat_detail()
        elif pilih == "2" and users[current_user]["role"] == "user":
            buat_post()
            return
        elif pilih == "0":
            current_user = None
            return
        else:
            print("Pilihan tidak valid")

# DETAIL POSTINGAN

def lihat_detail():
    if not posts:
        return

    idx = int(input("Masukkan ID permintaan: "))
    if idx >= len(posts):
        print("ID tidak valid")
        return

    p = posts[idx]
    while True:
        print("\n=== DETAIL PERMINTAAN ===")
        print("Nama barang:", p["nama"])
        print("Merek:", p["merek"])
        print("Tahun:", p["tahun"])
        print("Deskripsi:", p["deskripsi"])
        print("Kontak user:", p["kontak"])



# MENU AWAL

while True:
    print("\n=== MENU AWAL ===")
    print("1 Register")
    print("2 Login")
    print("3 Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        register()
    elif pilih == "2":
        login()
    elif pilih == "3":
        print("Keluar aplikasi")
        break
    else:
        print("Pilihan tidak valid")
