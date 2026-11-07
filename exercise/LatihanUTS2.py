print("* * * Ujian Tengah Semester 20261 * * *")
print("---------------------------------------")
nama = input("Masukkan Nama Anda: ").upper()
print("Selamat Datang,", nama)
status_dataDiri = False
while True:
    print("\n === Aplikasi Perhitungan Kalori dan BMI ===\n")
    print("1. Masukkan Data Diri")
    print("2. Hitung Kebutuhan Kalori")
    print("3. Hitung BMI")
    print("4. Keluar")
    pilihan = int(input("Pilihan Anda: "))
    while True:
        if pilihan == 1:
        # BERAT BADAN
            status_dataDiri = True
            bb = int(input("Masukkan Berat Badan (Kg): "))
            tb = int(input("Masukkan Tinggi Badan (Cm): "))
            while True:
                jk = input("Masukkan Jenis Kelamin (P/W): ").lower()
                if jk != "p" and jk != "w":
                    print("Jenis Kelamin Harus (P)ria atau (W)anita")
                    continue
                break
            usia =  int(input("Masukkan Usia: "))
            break
            
    
        elif pilihan == 2:
            if status_dataDiri:
                bmr_pria = 88.362 + (13.397 * bb) + (4.799 * tb) - (5.677 * usia)
                bmr_wanita = 447.593 + (9.247 * tb) + (3.098 * tb) - (4.330 * usia)
                if jk == "p":
                    print(f"Kebutuhan Kalori Harian Anda adalah: {bmr_pria:.0f} Kalori")
                elif jk == "w":
                    print("Kebutuhan Kalori Harian Anda adalah: ", bmr_wanita, "Kalori")
            else:
                print("\nTidak dapat melanjutkan, masukkan data diri terlebih dahulu!")
            break
        elif pilihan == 3:
            if status_dataDiri:
                tb_m = tb / 100
                bmi = bb / (tb_m * tb_m)
                print(f"\nBMI Anda: {bmi:.2f}")
                if bmi < 18.5:
                    print("Kategori BMI: Kurus")
                if bmi >= 18.5 and bmi <= 24.9:
                    print("Kategori BMI: Normal")
                if bmi >= 25 and bmi <= 29.9:
                    print("Kategori BMI: Gemuk")
                if bmi >= 30:
                    print("Kategori BMI: Obesitas")
                break
            

        elif pilihan == 4:
            exit()

