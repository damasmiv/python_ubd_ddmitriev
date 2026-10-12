print("Program Penghitung Indeks Prestasi Semester (IPS)")
matkul = int(input("Masukkan Jumlah Mata Kuliah: "))

totalbobot = 0
for i in range(1, matkul +1):
    print(f"Mata Kuliah {i}:")
    nilai = input("Masukkan Nilai A/B/C/D: ").upper()
    if nilai == "A":
        bobot = 4
    if nilai == "B":
        bobot = 3
    if nilai == "C":
        bobot = 2
    if nilai == "D":
        bobot = 1
    totalbobot += bobot
    ips = totalbobot / matkul

if ips >= 3.5 and ips <= 4.0:
    status = "Lulus dengan Pujian Besar (Cum Laude)"
elif ips >= 3.0 and ips <= 3.40:
    status = "Lulus dengan Pujian (With Honors)"
elif ips >= 2.5 and ips <= 2.99:
    status = "Lulus dengan Baik (Satisfactory)"
elif ips <= 2.5:
    status = "Tidak Lulus (Failed)"

print("Indeks Prestasi Semester (IPS): ", ips)
print("Status Kelulusan: ", status)