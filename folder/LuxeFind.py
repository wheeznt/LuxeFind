users = {}
mediators = {}
requests = []


# ========== FILE DATABASE ==========
def load_requests():
    try:
        with open("requests.txt", "r") as f:
            for line in f:
                email, barang, desc, status = line.strip().split(";")
                requests.append({
                    "email": email,
                    "barang": barang,
                    "deskripsi": desc,
                    "status": status
                })
    except FileNotFoundError:
        pass


def save_request(email, barang, deskripsi, status="Pending"):
    with open("requests.txt", "a") as f:
        f.write(f"{email};{barang};{deskripsi};{status}\n")

def load_data():
    # load users
    try:
        with open("users.txt", "r") as f:
            for line in f:
                email, pwd = line.strip().split(";")
                users[email] = pwd
    except FileNotFoundError:
        pass

    # load mediators
    try:
        with open("mediators.txt", "r") as f:
            for line in f:
                email, pwd = line.strip().split(";")
                mediators[email] = pwd
    except FileNotFoundError:
        pass


def save_user(email, password):
    with open("users.txt", "a") as f:
        f.write(f"{email};{password}\n")


def save_mediator(email, password):
    with open("mediators.txt", "a") as f:
        f.write(f"{email};{password}\n")

def save_all_requests():
    with open("requests.txt", "w") as f:
        for r in requests:
            f.write(f"{r['email']};{r['barang']};{r['deskripsi']};{r['status']}\n")


# ========== AUTHENTICATION ==========

def register_user():
    print("\n=== REGISTER USER ===")
    email = input("Email: ")
    password = input("Password: ")

    if email in users:
        print("Email sudah terdaftar!\n")
    else:
        users[email] = password
        save_user(email, password)
        print("Registrasi User berhasil!\n")


def register_mediator():
    print("\n=== REGISTER MEDIATOR ===")
    email = input("Email: ")
    password = input("Password: ")

    if email in mediators:
        print("Email mediator sudah terdaftar!\n")
    else:
        mediators[email] = password
        save_mediator(email, password)
        print("Registrasi Mediator berhasil!\n")


def login_user():
    print("\n=== LOGIN USER ===")
    email = input("Email: ")
    password = input("Password: ")

    if email in users and users[email] == password:
        print("Login berhasil!\n")
        menu_user(email)
    else:
        print("Email atau password salah!\n")


def login_mediator():
    print("\n=== LOGIN MEDIATOR ===")
    email = input("Email: ")
    password = input("Password: ")

    if email in mediators and mediators[email] == password:
        print("Login mediator berhasil!\n")
        menu_mediator(email)
    else:
        print("Email atau password salah!\n")


# ========== FITUR USER ==========
def buat_request(email):
    print("\n=== BUAT PERMINTAAN BARANG ===")
    barang = input("Nama barang: ")
    deskripsi = input("Deskripsi barang: ")

    req = {
        "email": email,
        "barang": barang,
        "deskripsi": deskripsi,
        "status": "Pending"
    }
    requests.append(req)
    save_request(email, barang, deskripsi)  # default status Pending

    print("Permintaan berhasil dibuat!\n")


def lihat_request_user(email):
    print("\n=== PERMINTAAN SAYA ===")
    found = False
    for r in requests:
        if r["email"] == email:
            print(f"- {r['barang']} : {r['deskripsi']} (Status: {r['status']})")
            found = True
    if not found:
        print("Belum ada permintaan.\n")


def menu_user(email):
    while True:
        print("=== MENU USER ===")
        print("1. Buat permintaan barang")
        print("2. Lihat permintaan saya")
        print("3. Logout")

        pil = input("Pilih: ")
        if pil == "1":
            buat_request(email)
        elif pil == "2":
            lihat_request_user(email)
        elif pil == "3":
            break
        else:
            print("Pilihan tidak valid!\n")


# ========== FITUR MEDIATOR ==========
def menu_mediator(email):
    while True:
        print("=== MENU MEDIATOR ===")
        print("1. Lihat semua request")
        print("2. Approve/Reject request")
        print("3. Logout")

        pil = input("Pilih: ")

        if pil == "1":
            print("\n=== SEMUA PERMINTAAN USER ===")
            if not requests:
                print("Belum ada request!\n")
            else:
                for idx, r in enumerate(requests):
                    print(f"{idx+1}. {r['email']} meminta {r['barang']} : {r['deskripsi']} (Status: {r['status']})")
                print()

        elif pil == "2":
            if not requests:
                print("\nTidak ada request untuk diedit!\n")
                continue

            for idx, r in enumerate(requests):
                print(f"{idx+1}. {r['email']} - {r['barang']} ({r['status']})")

            try:
                pilihan = int(input("Pilih nomor permintaan: ")) - 1
                if pilihan < 0 or pilihan >= len(requests):
                    print("Nomor tidak valid!\n")
                    continue
            except:
                print("Input tidak valid!\n")
                continue

            print("1. Approve")
            print("2. Reject")
            aksi = input("Pilih aksi: ")

            if aksi == "1":
                requests[pilihan]["status"] = "Approved"
            elif aksi == "2":
                requests[pilihan]["status"] = "Rejected"
            else:
                print("Pilihan aksi salah!\n")
                continue

            save_all_requests()
            print("Status berhasil diperbarui!\n")

        elif pil == "3":
            break

        else:
            print("Pilihan tidak valid!\n")


# ========== MENU UTAMA ==========
def main():
    load_data()
    load_requests()
    while True:
        print("=== LUXEFIND CLI ===")
        print("1. Login User")
        print("2. Register User")
        print("3. Login Mediator")
        print("4. Register Mediator")
        print("5. Keluar")

        menu = input("Pilih menu: ")

        if menu == "1": login_user()
        elif menu == "2": register_user()
        elif menu == "3": login_mediator()
        elif menu == "4": register_mediator()
        elif menu == "5":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!\n")


main()