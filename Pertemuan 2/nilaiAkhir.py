print("================================")
print("Nilai Akhir Mahasiswa")
print("================================")
nama = input("Masukkan nama Anda: ")
nim = input("Masukkan NIM Anda: ")
uts = int(input("Masukkan nilai UTS: "))
uas = int(input("Masukkan nilai UAS: "))
tugas = int(input("Masukkan nilai Tugas: "))
proyek = int(input("Masukkan nilai Proyek: "))

uts_ = uts * 0.3
uas_ = uas * 0.4
tugas_ = tugas * 0.15
proyek_ = proyek * 0.15

print("Mahasiswa yang bernama : ", nama )
print("dengan  nilai presentasi yang dihasilkan")
print("\tNilai UTS * 30% : ", uts_)
print("\tNilai UAS * 40% : ", uas_)
print("\tNilai Tugas * 15% : ", tugas_)
print("\tNilai Proyek * 15% : ", proyek_)

print("Nilai Akhir yang diperoleh oleh mahasiswa dengan nama ",nama, "NIM:", nim, ":", uts_ + uas_ + tugas_ + proyek_ / 4) 
