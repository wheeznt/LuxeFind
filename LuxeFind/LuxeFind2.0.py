users = {}
requests = []
proposals = []
chats = []

current_user = None

# AUTH

def register():
    email = input("Email: ")
    password = input("Password: ")
    if email in users:
        print("Email sudah terdaftar")
        return
    users[email] = password
    print("Registrasi berhasil")

def login():
    global current_user
    email = input("Masukkan email: ")
    password = input("Masukkan password: ")

    if email in users and users[email] == password:
        current_user = email
        print("Login berhasil! Selamat datang,", email)
        return True
    else:
        print("Email atau password salah!")
        return False

# REQUEST BARANG

def buat_permintaan():
    nama = input("Nama barang: ")
    detail = input("Detail barang: ")
    request = {
        "user": current_user,
        "nama": nama,
        "detail": detail,
        "status": "Menunggu mediator"
    }
    requests.append(request)
    print("Permintaan dibuat")

def lihat_permintaan():
    for i, r in enumerate(requests):
        print(i, r["nama"], r["status"])

# MEDIATOR

def kirim_proposal():
    lihat_permintaan()
    idx = int(input("Pilih ID permintaan: "))
    harga = int(input("Harga penawaran: "))
    proposal = {
        "request_id": idx,
        "mediator": current_user,
        "harga": harga,
        "status": "Menunggu persetujuan"
    }
    proposals.append(proposal)
    requests[idx]["status"] = "Ada penawaran"
    print("Proposal dikirim")

# PEMBAYARAN

def bayar():
    for i, p in enumerate(proposals):
        print(i, p)
    idx = int(input("Pilih ID proposal: "))
    proposals[idx]["status"] = "Dibayar"
    requests[proposals[idx]["request_id"]]["status"] = "Diproses"
    print("Pembayaran berhasil")

# PENGIRIMAN

def update_pengiriman():
    for i, r in enumerate(requests):
        print(i, r["nama"], r["status"])
    idx = int(input("ID permintaan: "))
    requests[idx]["status"] = "Dikirim"
    print("Status diperbarui")

# CHAT

def kirim_chat():
    pesan = input("Pesan: ")
    chats.append({"user": current_user, "pesan": pesan})
    print("Pesan terkirim")

def lihat_chat():
    for c in chats:
        print(c["user"], ":", c["pesan"])

# MENU

def menu_user():
    print("1 Buat permintaan barang")
    print("2 Lihat permintaan")
    print("3 Bayar")
    print("4 Chat")
    print("5 Logout")


def menu_mediator():
    print("1 Lihat permintaan")
    print("2 Kirim proposal")
    print("3 Update pengiriman")
    print("4 Chat")
    print("5 Logout")

def menu_setelah_login():
    while True:
        print("\n=== HALAMAN UTAMA ===")
        print("1 Menu User")
        print("2 Menu Mediator")
        print("3 Logout")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            menu_user()
            m = input("Pilih: ")
            if m == "1": buat_permintaan()
            elif m == "2": lihat_permintaan()
            elif m == "3": bayar()
            elif m == "4": kirim_chat(); lihat_chat()
            elif m == "5": return
        elif pilih == "2":
            menu_mediator()
            m = input("Pilih: ")
            if m == "1": lihat_permintaan()
            elif m == "2": kirim_proposal()
            elif m == "3": update_pengiriman()
            elif m == "4": kirim_chat(); lihat_chat()
            elif m == "5": return
        elif pilih == "3":
            logout()
            return
        else:
            print("Pilihan tidak valid")


def logout():
    global current_user
    current_user = None
    print("Logout berhasil")

while True:
    print("\n=== MENU UTAMA ===")
    print("1 Register")
    print("2 Login")
    print("3 Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        register()
    elif pilih == "2":
        if login():
            menu_setelah_login()
    elif pilih == "3":
        print("Terima kasih")
        break
    else:
        print("Pilihan tidak valid")