users = {}

def register():
    print("\n=== Register ===")
    email = input("Masukkan email: ")
    password = input("Masukkan password: ")

    if email in users:
        print("Email sudah terdaftar!")
    else:
        users[email] = password
        print("Registrasi berhasil!")

def login():
    print("\n=== Login ===")
    email = input("Masukkan email: ")
    password = input("Masukkan password: ")

    if email in users and users[email] == password:
        print("Login berhasil! Selamat datang,", email)
    else:
        print("Email atau password salah!")

def main():
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Register")
        print("2. Login")
        print("3. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == '1':
            register()
        elif pilih == '2':
            login()
        elif pilih == '3':
            print("Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()
