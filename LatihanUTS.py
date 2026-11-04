print("* * * Ujian Tengah Semester 20261 * * *")
print("---------------------------------------")
nama = input("Masukkan Nama Anda: ").upper()
print("Selamat Datang,", nama)

# HARGA
vbasic = 5000
# INPUT SECTION
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
            paket = int(input("Pilih Jenis Paket (1/2): "))
            status_paket = True
            if paket == 1:
                harga = 50000
            elif paket == 2:
                harga = 100000
            if paket != 1 and paket != 2:
                print("Pilihan paket tidak valid. Silakan pilih 1 atau 2.")
                continue
            break

        elif pilihan == 2:
            durasi = int(input("\nDurasi Berlangganan (1-12 bulan): "))
            status_durasi = True
            if durasi <= 0 or durasi > 12:
                print("Durasi berlangganan harus antara 1-12 bulan.")
                continue
            break
        elif pilihan == 3:
            jumlah_video = int(input("\nJumlah Video yang akan diakses: "))
            status_jumlah = True
            if jumlah_video <= 0:
                print("Jumlah video harus lebih dari 0.")
                continue
            break
        elif pilihan == 4:
            if status_durasi and status_jumlah and status_paket:
                biaya_paket_sebelum_diskon = harga * durasi
                biaya_video = vbasic if paket == 1 else 0
                totalBiayaKotor = biaya_paket_sebelum_diskon + (jumlah_video * biaya_video)
                total_video = biaya_video * jumlah_video

                #diskon
                diskon_1 = 0
                diskon_2 = 0
                if durasi > 3:
                    diskon_1 = biaya_paket_sebelum_diskon * 10/100
                if jumlah_video > 20:
                    diskon_2 =  totalBiayaKotor * 5/100
                totalDiskon = diskon_1 + diskon_2
                total_berlangganan = totalBiayaKotor - totalDiskon
                print("\n=== Detail Berlangganan ===")
                print("Jenis Paket: ", "Basic" if paket == 1 else "Premium")
                print("Durasi Berlangganan: ", durasi, "bulan")
                print(f"Biaya Paket: Rp {biaya_paket_sebelum_diskon:,.0f}")
                print(f"Biaya Video: Rp {total_video:,.0f}")
                print(f"Total Diskon: Rp {totalDiskon:,.0f}")
                print(f"Total Biaya Berlangganan: Rp {total_berlangganan:,.0f}")
            else:
                print("\nTidak dapat menampilkan Infomasi Detail berlangganan karena belum lengkap mengisi Data")
            break
        elif pilihan == 5:
            print("Terima Kasih telah menggunakan Aplikasi Berlangganan ini.")
            exit()