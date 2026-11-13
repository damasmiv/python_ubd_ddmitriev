def hitung_total(paket, durasi, jumlahvideo):
    if paket == 1:
        nama_paket = "Basic"
        harga_per_bulan = 50000
        harga_per_video = 5000
    elif paket == 2:
        nama_paket = "Premium"
        harga_per_bulan = 100000
        harga_per_video = 0
    else:
        return None

    biayapaket = harga_per_bulan * durasi
    biayavideo = harga_per_video * jumlahvideo

    diskonpaket = 0
    if durasi > 3:
        diskonpaket = biayapaket * 0.1
    totalsementara = biayapaket + biayavideo - diskonpaket
    diskontambahan = 0
    if jumlahvideo > 20:
        diskontambahan = totalsementara * 0.05
    totaldiskon = diskonpaket + diskontambahan
    totalbiaya = totalsementara - diskontambahan
    print("\n=== Detail Berlangganan ===")
    print(f"Jenis Paket: {nama_paket}")
    print(f"Durasi Berlangganan: {durasi} bulan")
    print(f"Biaya Paket: Rp {biayapaket:,.0f}")
    print(f"Biaya Video: Rp {biayavideo:,.0f}")
    print(f"Total Diskon: Rp {totaldiskon:,.0f}")
    print(f"Total Biaya Berlangganan: Rp {totalbiaya:,.0f}")


print("* * * UJIAN TENGAH SEMESTER 20261 * * *")
print("---------------------------------------")
nama = input("Masukkan Nama Anda: ").upper()
print(f"Selamat Datang, {nama}\n")
status_paket = False
status_durasi = False
status_video = False
while True:
    print("\n=== APLIKASI BERLANGGANAN VIDEO STREAMING ===")
    print("Menu:")
    print("1. Pilih Paket")
    print("2. Durasi Berlangganan")
    print("3. Jumlah Video")
    print("4. Lihat Hasil Berlangganan")
    print("5. Keluar")
    pilihan = int(input("\nPilihan Anda: "))
    if pilihan == 1:
        while True:
            print("\nJenis Paket:")
            print("1. Basic")
            print("2. Premium")
            paket = int(input("\nPilih Jenis Paket 1/2: "))
            status_paket = True
            if paket != 1 and paket != 2:
                print("\nPaket tidak valid! Pilih 1 atau 2.")
                continue
            break
    elif pilihan == 2:
        while True:
            durasi = int(input("\nDurasi Berlangganan: "))
            status_durasi = True
            if durasi <= 0 or durasi > 12:
                print("\nDurasi Harus Antara 1 - 12 Bulan!")
                continue
            break
    elif pilihan == 3:
        while True:
            jumlahvideo = int(input("\nJumlah Video yang akan diakses: "))
            status_video = True
            if jumlahvideo <= 0:
                print("\nJumlah Video harus lebih dari 0!")
                continue
            break
    elif pilihan == 4:
        if status_durasi and status_paket and status_video:
            hitung_total(paket, durasi, jumlahvideo)
        else:
            print("\nTidak dapat melihat hasil, mohon untuk melengkapi data terlebih dahulu!")
    elif pilihan == 5:
        print("\nTerima Kasih telah menggunakan Aplikasi!\n")
        exit()
    else:
        print("\nPilihan tidak valid! silahkan pilih 1-5!")


    


