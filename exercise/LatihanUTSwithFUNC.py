def hitung_detailpaket(jenispaket, durasi, jumlahvideo):
    if jenispaket == 1:
        nama_paket = "Basic"
        harga_per_bulan = 50000
        harga_per_video = 5000
    elif jenispaket == 2:
        nama_paket = "Premium"
        harga_per_bulan = 100000
        harga_per_video = 0
    else:
        return None

    biayapaket = harga_per_bulan * durasi
    biayavideo = jumlahvideo * harga_per_video

    diskonpaket = 0 
    if durasi > 3:
        diskonpaket = biayapaket * 0.1
    total_sementara = biayapaket + biayavideo - diskonpaket
    diskontambahan = 0
    if jumlahvideo > 20:
        diskontambahan = total_sementara * 0.05

    totaldiskon = diskonpaket + diskontambahan
    totalbiaya = total_sementara - diskontambahan

    print(f"\n=== Detail Berlangganan ===")
    print(f"Jenis Paket: {nama_paket}")
    print(f"Durasi Berlangganan: {durasi} bulan")
    print(f"Biaya Paket: Rp {biayapaket:,.0f}")
    print(f"Biaya Video: Rp {biayavideo:,.0f}")
    print(f"Total Diskon: Rp {totaldiskon:,.0f}")
    print(f"Total Biaya Berlangganan: Rp {totalbiaya:,.0f}")

print("* * * Ujian Tengah Semester 20261 * * *")
print("---------------------------------------")
nama = input("Masukkan Nama Anda: ").upper()
print("Selamat Datang,", nama)
status_paket = False
status_durasi = False
status_jumlah = False
while True:
    print("\n=== Aplikasi Berlangganan Video Streaming ===")
    print("Menu:")
    print("1. Pilih Paket")
    print("2. Durasi Berlangganan")
    print("3. Jumlah Video")
    print("4. Lihat Hasil Berlangganan")
    print("5. Keluar")
    pilihan = int(input("Pilihan Anda: "))
    while True:

        if pilihan == 1:
            print("\nJenis Paket:")
            print("1. Basic")
            print("2. Premium")
            jenispaket = int(input("\nPilihan Jenis Paket 1/2: "))
            status_paket = True
            if jenispaket != 1 and jenispaket != 2:
                print("\nPaket tidak valid, silahkan pilih 1/2")
                continue
            break

        elif pilihan == 2:
            durasi = int(input("\nDurasi Berlangganan: "))
            status_durasi = True
            if durasi <= 0 or durasi > 12:
                print("\nDurasi harus antara 1 - 12 Bulan!")
                continue
            break

        elif pilihan == 3:
            jumlahvideo = int(input("Jumlah Video yang akan diakses: "))
            status_jumlah = True
            if jumlahvideo <= 0:
                print("\nJumlah Video harus lebih dari 0!")
                continue
            break
        elif pilihan == 4:
            if status_jumlah and status_durasi and status_paket:
                hasil = hitung_detailpaket(jenispaket, durasi, jumlahvideo)
                print(hasil)
            else:
                print("\nTidak dapat menampilkan informasi total, tolong masukkan detail terlebih dahulu!")
            break
        elif pilihan == 5:
            print("\nTerima kasih sudah menggunakan Aplikasi")
            exit()



                
           
                



