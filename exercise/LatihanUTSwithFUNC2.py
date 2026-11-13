def hitung_bmr(bb, tb, jenis_kelamin, usia):
    if jenis_kelamin == "P":
        bmr = 88.362 + (13.397 * bb) + (4.799 * tb) - (5.677 * usia)
    elif jenis_kelamin == "W":
        bmr = 447.593 + (9.247 * bb) + (3.098 * tb) - (4.330 * usia)
    print(f"\nKebutuhan Kalori Harian Anda: {bmr:.0f} Kalori")

def hitung_bmi(bb, tb):
    bmi = bb / ((tb/100) ** 2)
    if bmi < 18.5:
        kategori = "Kurus"
    elif bmi < 25:
        kategori = "Normal"
    elif bmi < 30:
        kategori = "Gemuk"
    else:
        kategori = "Obesitas"
    print(f"\nBMI Anda: {bmi:.2f}")
    print(f"Kategori BMI: {kategori}")

print("*** UJIAN TENGAH SEMESTER 20261 ***")
print("-----------------------------------")
nama = input("Masukkan Nama Anda: ").upper()
print("Selamat Datang,",nama)
status_datadiri = False
while True:
    print("\n=== Aplikasi Perhitungan Kalori dan BMI ===")
    print("\nMenu:")
    print("1. Masukkan Data Diri")
    print("2. Hitung Kebutuhan Kalori")
    print("3. Hitung BMI")
    print("4. Keluar")
    pilihan = int(input("\nPilihan Anda: "))
    if pilihan == 1:
        bb = int(input("Masukkan Berat Badan (Kg): "))
        tb = int(input("Masukkan Tinggi Badan (CM): "))
        while True:
            jenis_kelamin = input("Masukkan Jenis Kelamin (P/W): ").upper()
            if jenis_kelamin != "P" and jenis_kelamin != "W":
                print("Jenis Kelamin harus (P)ria / (W)anita!")
            else:
                break
        usia = int(input("Masukkan Usia: "))
        status_datadiri = True
    elif pilihan == 2:
        if status_datadiri:
            hitung_bmr(bb, tb, jenis_kelamin, usia)
        else:
            print("\nMohon Untuk Melengkapi Data Diri agar dapat menghitung!")
    elif pilihan == 3:
        if status_datadiri:
            hitung_bmi(bb, tb)
        else:
            print("\nMohon Untuk Melengkapi Data Diri agar dapat menghitung!")
    elif pilihan == 4:
        print("Terima Kasih telah menggunakan Aplikasi Penghitung BMR dan BMI!")
        exit()
    else:
        print("\nPilihan tidak valid, silahkan pilih 1-4!")