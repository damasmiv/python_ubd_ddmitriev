print("Selamat datang di Aplikasi Perpustakaan UBD!")
print("\nMenu Perpustakaan:")
print("1. Daftar Buku")
print("2. Cari Buku")
print("3. Keluar")

while True:
    userinput = int(input("Pilihan Menu (1/2/3): "))
    if userinput == 1:
        print("\nDaftar Buku:")
        print("1. Harry Potter (J.K. Rowling)")
        print("2. Lord of the Rings (J.R.R. Tolkien)")
        print("3. To Kill a Mockingbird (Harper Lee)")
        print("4. The Great Gatsby (F. Scott Fitzgerald)")

    elif userinput == 2:
        judul_buku = input("Masukkan judul buku yang ingin dicari: ")
        if judul_buku.lower() == "harry potter":
            print("Buku 'Harry Potter' ditemukan dalam perpustakaan. Penulis: J.K. Rowling")

        elif judul_buku.lower() == "lord of the rings":
            print("Buku 'Lord of the Rings' ditemukan dalam perpustakaan. Penulis: J.R.R. Tolkien")

        elif judul_buku.lower() == "to kill a mockingbird":
            print("Buku 'To Kill a Mockingbird' ditemukan dalam perpustakaan. Penulis: Harper Lee")

        elif judul_buku.lower() == "the great gatsby":
            print("Buku 'The Great Gatsby' ditemukan dalam perpustakaan. Penulis: Scott Fitzgerald")

        else:
            print(f"Buku '{judul_buku}' tidak ditemukan di perpustakaan.")
    elif userinput == 3:
        print("Terima Kasih Atas Penggunaan Aplikasi Perpustakaan UBD!")
        exit()
    else:
        print("Pilihan menu tidak valid. Silakan pilih menu 1, 2, atau 3.")


