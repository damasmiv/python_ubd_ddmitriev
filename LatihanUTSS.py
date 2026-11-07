# FUNGSI
def hitung_total(paket, durasi, jumlah_video):
    if paket == 1:
        namapaket = "Basic"
        harga_per_bulan = 50000
        harga_per_video = 5000
    elif paket == 2:
        namapaket = "Premium"
        harga_per_bulan = 100000
        harga_per_video = 0
    else:
        return None
    
    biayapaket = harga_per_bulan * durasi
    biayavideo = harga_per_video * jumlah_video

    diskonpaket = 0
    if durasi > 3:
        diskonpaket = biayapaket * 0.1
    total_sementara = biayapaket + biayavideo - diskonpaket
    diskontambahan = 0
    if jumlah_video > 20:
        diskontambahan = total_sementara * 0.05
    totaldiskon = diskonpaket + diskontambahan
    totalbiaya = total_sementara - diskontambahan
    print(f"\n=== Detail Berlangganan ===")
    print(f"Jenis Paket: {namapaket}")
    print(f"Durasi Berlangganan: {durasi} bulan")
    print(f"Biaya Paket: Rp {biayapaket:,.0f}")
    print(f"Biaya Video: Rp {biayavideo:,.0f}")
    print(f"Total Diskon: Rp {totaldiskon:,.0f}")
    print(f"Total Biaya Berlangganan: Rp {totalbiaya:,.0f}")

    


#TAMPILAN
print("*** UJIAN TENGAH SEMESTER 20261 ***")
print("-----------------------------------")
nama = input("Masukkan Nama Anda: ").upper()
print("Selamat Datang,",nama)
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
    userInput = int(input("\nPilihan Anda: "))
    
    if userInput == 1:
        status_paket = True
        print("Jenis Paket:")
        print("1. Basic")
        print("2. Premium")
        while True:
            paket = int(input("Pilih Jenis Paket (1/2): "))
            if paket != 1 and paket != 2:
                print("Paket Tidak Valid! pilih 1/2!")
            else:
                break      
    elif userInput == 2:
        status_durasi = True
        while True:
            durasi = int(input("Durasi Berlangganan (1 - 12 Bulan): "))
            if durasi <= 0 or durasi >= 12:
                print("Durasi harus antara 1-12 bulan!")
            else:
                break
    elif userInput == 3:
        status_jumlah = True
        jumlah_video = int(input("Jumlah Video yang akan diakses: "))
    elif userInput == 4:
        if status_jumlah and status_durasi and status_jumlah:
            hitung_total(paket, durasi, jumlah_video)
        else:
            print("Mohon untuk melengkapi data sebelum melihat total!")
    elif userInput == 5:
        print("Terima Kasih telah menggunakan aplikasi kami!")
        exit()
    else:
        print("Pilihan tidak valid! silahkan pilih 1-5!")
        continue            
            

