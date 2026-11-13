def hitung_bmr(bb, tb, jk, usia):
    if jk == "P":
        bmr = 88.362 + (13.397 * bb) + (4.799 * tb) - (5.677 * usia)
    elif jk == "W":
        bmr = 447.593 + (9.247 * bb) + (3.098 * tb) - (4.330 * usia)
    print(f"Kebutuhan Kalori Harian Anda: {bmr:.2f}")
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
print("* * * UJIAN TENGAH SEMESTER 20261 * * *")
print("---------------------------------------")
nama = input("Masukkan Nama Anda: ").upper()
print(f"Selamat Datang, {nama}")
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
        bb = int(input("Masukkan Berat Badan (KG): "))
        tb = int(input("Masukkan Tinggi Badan (CM): "))
        while True:
            jk = input("Masukkan Jenis Kelamin (P/W): ").upper()
            if jk != "P" and jk != "W":
                print("Jenis Kelamin harus (P)ria / (W)anita!")
            else:
                break
        usia = int(input("Masukkan Usia: "))
        status_datadiri = True
    elif pilihan == 2:
        if status_datadiri:
            hitung_bmr(bb, tb, jk, usia)
        else:
            print("Mohon Untuk Melengkapi data diri untuk menghitung Kalori")
    elif pilihan == 3:
        if status_datadiri:
            hitung_bmi(bb, tb)
        else:
            print("Mohon Untuk Melengkapi data diri untuk menghitung BMI")
    elif pilihan == 4:
        chose = input("Apakah anda yakin ingin keluar? (Y/N): ").upper()
        if chose == "Y":
            print("Terima Kasih telah menggunakan Aplikasi kami!")
            exit()
        else:
            continue
    else:
        print("\nPilihan tidak valid! silahkan pilih 1-4!")