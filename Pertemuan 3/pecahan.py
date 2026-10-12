print("===================================")
print("Kalkulator Susunan Mata Uang Rupiah")
print("===================================")
nama = input("Masukkan Nama: ")
uang = int(input(f"Masukkan Jumlah uang (Dalam Rupiah): "))

#LOGIC
u100k = uang // 100000
sisa = uang % 100000

u50k = sisa // 50000
sisa = sisa % 50000

u20k = sisa // 20000
sisa = sisa % 20000

u10k = sisa // 10000
sisa = sisa % 10000

u5k = sisa // 5000
sisa = sisa % 5000

u2k = sisa // 2000
sisa = sisa % 2000

u1k = sisa // 1000
sisa = sisa % 1000

u500p = sisa // 500
sisa = sisa % 500

u200p = sisa // 200
sisa = sisa % 200

u100p = sisa // 100
sisa = sisa % 100
print("Jumlah Uang", nama, ": ", uang)
print("Kombinasi Uang yang Mungkin adalah: ")
print(u100k, "Lembar uang 100 ribu Rupiah.")
print(u50k, "Lembar uang 50 ribu Rupiah.")
print(u20k, "Lembar uang 20 ribu Rupiah.")
print(u10k, "Lembar uang 10 ribu Rupiah.")
print(u5k, "Lembar uang 5 ribu Rupiah.")
print(u2k, "Lembar uang 2 ribu Rupiah.")
print(u1k, "Lembar uang 1 ribu Rupiah.")
print(u500p, "Keping uang 500 Rupiah.")
print(u200p, "Keping uang 200 Rupiah.")
print(u100p, "Keping uang 100 Rupiah.")