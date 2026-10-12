print("----------------------------------")
print("Program Penghitungan Gaji Karyawan")
print("----------------------------------")

# USER INPUT SECTION

jabatan = input("Kategori Jabatan (M / S / K): ").upper()
if jabatan == "M":
        jenis = "Manajer"
        
elif jabatan == "S":
        jenis = "Supervisor"
        
elif jabatan == "K":
        jenis = "Karyawan Biasa"
        
else:
    print("Kategori Jabatan tidak Valid!")
    exit()


pendidikan = input("Kategori Pendidikan (SMA / D3 / S1): ").upper()
if pendidikan == "SMA":
        pddk = "SMA"
        
elif pendidikan == "D3":
        pddk = "D3"
       
elif pendidikan == "S1":
        pddk = "S1"
        
else:
        print("Kategori Pendidikan tidak Valid!")
        exit()

durasi = int(input("Lama Bekerja (Dalam Tahun): "))

# HONOR LEMBUR
honor_lembur = 0
total_honor = 0
jam_lembur = "-"

if jabatan == "K":
    jam_lembur = int(input("Lama Jam Lembur: "))
    if durasi <= 5:
        honor_lembur = 50000
    elif durasi >= 6 and durasi <= 10:
        honor_lembur = 100000
    else:
        honor_lembur = 150000
    total_honor = jam_lembur * honor_lembur
else:
    print("Honor Jam Lembur hanya diberikan kepada Karyawan Biasa!")

# GAJI POKOK
gaji_pokok = 0
if jabatan == "K":
    gaji_pokok = 7500000
elif jabatan == "M":
    gaji_pokok = 15000000
elif jabatan == "S":
    gaji_pokok = 10000000

# GAJI TAMBAHAN
gaji_tambahan = 0
if pendidikan == "SMA":
    gaji_tambahan = 1000000
elif pendidikan == "D3":
    gaji_tambahan = 2000000
elif pendidikan == "S1":
    gaji_tambahan = 3000000

# KALKULASI

total_gaji = gaji_pokok + gaji_tambahan + total_honor

# OUTPUT SECTION

print("\nInformasi Karyawan:")
print("Kategori Jabatan: ",jenis)
print("Kategori Pendidikan: ",pddk)
print("Lama Bekerja: ",durasi, "Tahun")
print("Lama Jam Lembur: ",jam_lembur, "Jam")
print(f"Honor Lembur per Jam: Rp.{honor_lembur:,.0f}")
print(f"Total Gaji Karyawan: Rp.{total_gaji:,.0f}")


