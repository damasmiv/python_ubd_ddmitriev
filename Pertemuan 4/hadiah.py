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
elif rata_rata <= 70:
    hadiah = "Hiburan"


print("\n=================")
print("Hasil Perhitungan")
print("=================\n")

print("Nama Siswa: ", nama)
print("Nilai Rata-Rata: ", rata_rata)

print("\nSelamat, Anda mendapatkan Hadiah:\n",hadiah)





