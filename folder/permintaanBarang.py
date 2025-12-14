requests = []

# ===== FILE HANDLING =====
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


def save_all_requests():
    with open("requests.txt", "w") as f:
        for r in requests:
            f.write(f"{r['email']};{r['barang']};{r['deskripsi']};{r['status']}\n")


# ===== FITUR PERMINTAAN BARANG =====
def buat_request():
    print("\n=== BUAT PERMINTAAN BARANG ===")
    email = input("Email pemohon: ")
    barang = input("Nama barang: ")
    deskripsi = input("Deskripsi: ")

    req = {
        "email": email,
        "barang": barang,
        "deskripsi": deskripsi,
        "status": "Pending"
    }

    requests.append(req)
    save_request(email, barang, deskripsi)
    print("Permintaan berhasil dibuat!\n")


def lihat_requests():
    print("\n=== DAFTAR PERMINTAAN ===")
    if not requests:
        print("Belum ada permintaan.\n")
        return

    for i, r in enumerate(requests):
        print(f"{i+1}. {r['email']} - {r['barang']} ({r['status']})")
    print()


def update_status():
    lihat_requests()
    if not requests:
        return

    try:
        idx = int(input("Pilih nomor permintaan: ")) - 1
        if idx < 0 or idx >= len(requests):
            print("Nomor tidak valid!\n")
            return
    except:
        print("Input tidak valid!\n")
        return

    print("1. Approve")
    print("2. Reject")
    aksi = input("Pilih aksi: ")

    if aksi == "1":
        requests[idx]["status"] = "Approved"
    elif aksi == "2":
        requests[idx]["status"] = "Rejected"
    else:
        print("Pilihan tidak valid!\n")
        return

    save_all_requests()
    print("Status berhasil diperbarui!\n")


# ===== CLI MENU =====
def main():
    load_requests()

    while True:
        print("=== CLI PERMINTAAN BARANG ===")
        print("1. Buat permintaan barang")
        print("2. Lihat semua permintaan")
        print("3. Approve / Reject permintaan")
        print("4. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            buat_request()
        elif pilih == "2":
            lihat_requests()
        elif pilih == "3":
            update_status()
        elif pilih == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!\n")


main()
