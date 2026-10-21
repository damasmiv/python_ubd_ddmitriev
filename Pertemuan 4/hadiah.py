print("========================")
print("Program Hitung Rata-Rata")
print("========================\n")

nama = input("Masukkan Nama Siswa: ")
nilai1 = int(input("Masukkan Nilai Pertandingan I: "))
nilai2 = int(input("Masukkan Nilai Pertandingan II: "))
nilai3 = int(input("Masukkan Nilai Pertandingan III: "))

#LOGIC
rata_rata = (nilai1 + nilai2 + nilai3) / 3

if rata_rata >= 85: 
    hadiah = "Komputer"
elif rata_rata >= 70:
    hadiah = "Uang Tunai Sebesar Rp.500,000"
else:
    hadiah = "Hiburan"


print("\n=================")
print("Hasil Perhitungan")
print("=================\n")

print("Nama Siswa: ", nama)
print(f"Nilai Rata-Rata: {rata_rata:.1f}")

print("\nSelamat, Anda mendapatkan Hadiah:",hadiah)s





