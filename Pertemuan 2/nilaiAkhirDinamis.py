print("================================")
print("Nilai Akhir Mahasiswa")
print("================================")
nama = input("Masukkan nama Anda: ")
nim = input("Masukkan NIM Anda: ")
uts = int(input("Masukkan bobot UTS (dalam persentase): "))
uas = int(input("Masukkan bobot UAS (dalam persentase): "))
tugas = int(input("Masukkan bobot Tugas (dalam persentase): "))
proyek = int(input("Masukkan bobot Proyek (dalam persentase): "))
nilai_uts = int(input("Masukkan nilai UTS: "))
nilai_uas = int(input("Masukkan nilai UAS: "))
nilai_tugas = int(input("Masukkan nilai Tugas: "))
nilai_proyek = int(input("Masukkan nilai Proyek: "))

bobot_uts = nilai_uts*uts / 100
bobot_uas = nilai_uas*uas / 100
bobot_tugas = nilai_tugas*tugas / 100
bobot_proyek = nilai_proyek*proyek / 100

hasil_akhir = bobot_uts + bobot_uas + bobot_tugas + bobot_proyek / 4

print("Mahasiswa yang bernama : ", nama )
print("dengan  nilai presentasi yang dihasilkan")
print("\tNilai UTS * ", bobot_uts, "% : ", nilai_uts)
print("\tNilai UAS * ", bobot_uas, "% : ", nilai_uas)
print("\tNilai Tugas * ", bobot_tugas, "% : ", nilai_tugas)
print("\tNilai Proyek * ", bobot_proyek, "% : ", nilai_proyek)

print("Nilai akhir yang diperoleh Mahasiswa: ", nama, "Nim: ", nim, "Adalah : ", hasil_akhir)



