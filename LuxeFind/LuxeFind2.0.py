users = {}
posts = []
current_user = None

USERS_FILE = "users.txt"
POSTS_FILE = "posts.txt"

# ================= LOAD & SAVE =================

def load_users():
    try:
        with open(USERS_FILE, "r") as file:
            for line in file:
                email, password, role = line.strip().split("|")
                users[email] = {
                    "password": password,
                    "role": role
                }
    except FileNotFoundError:
        pass


def save_user(email, password, role):
    with open(USERS_FILE, "a") as file:
        file.write(f"{email}|{password}|{role}\n")


def load_posts():
    try:
        with open(POSTS_FILE, "r") as file:
            for line in file:
                user, nama, merek, tahun, deskripsi, kontak = line.strip().split("|")
                posts.append({
                    "user": user,
                    "nama": nama,
                    "merek": merek,
                    "tahun": tahun,
                    "deskripsi": deskripsi,
                    "kontak": kontak
                })
    except FileNotFoundError:
        pass


def save_post(post):
    with open(POSTS_FILE, "a") as file:
        file.write(
            f"{post['user']}|{post['nama']}|{post['merek']}|{post['tahun']}|{post['deskripsi']}|{post['kontak']}\n"
        )

# ================= AUTH =================

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

    save_user(email, password, role)
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

# ================= POSTING =================

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
    save_post(post)
    print("Postingan berhasil ditambahkan")

# ================= BERANDA =================

def beranda():
    while True:
        print("\n=== BERANDA ===")

        if not posts:
            print("Belum ada permintaan barang")
        else:
            for i, p in enumerate(posts):
                print(f"{i}. {p['nama']} | {p['merek']} | {p['tahun']}")

        print("Menu")
        print("1 Lihat detail permintaan")

        if users[current_user]["role"] == "user":
            print("2 Buat permintaan barang")
            print("3 Logout")
        else:
            print("2 Logout")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            lihat_detail()
        elif pilih == "2" and users[current_user]["role"] == "user":
            buat_post()
        elif pilih == "2" and users[current_user]["role"] == "mediator":
            logout()
            return
        elif pilih == "3":
            logout()
            return
        else:
            print("Pilihan tidak valid")

# ================= DETAIL =================

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

        print("Menu")
        print("1 Kembali ke beranda")

        pilih = input("Pilih menu: ")
        if pilih == "1":
            return

# ================= LOGOUT =================

def logout():
    global current_user
    current_user = None
    print("Logout berhasil")

# ================= PROGRAM START =================

load_users()
load_posts()

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
