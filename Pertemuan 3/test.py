# Meminta input nilai A dari pengguna
a = int(input("Masukkan Nilai A = "))
# Melakukan operasi perbandingan dan pemberian nilai boolean pada variabel b
b = (a + 4 < 10)
# Menggunakan operator NOT (!) untuk menghasilkan nilai boolean yang berlawanan
c = not b
# Menampilkan hasil operasi
print("Program Ekspresi NOT ")
print(f"Nilai A = {a}")
print(f"Nilai b = (a + 4 < 10) = {b}")
print(f"Nilai c = !(b) = {c}")