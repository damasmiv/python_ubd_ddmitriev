print("===================================")
print("Kalkulator Susunan Mata Uang Rupiah")
print("===================================")
jumlah_uang = int(input("Masukkan Jumlah Uang Ali: "))

print("Jumlah Uang Ali: ", jumlah_uang)

#LOGIC
pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]

print("Kombinasi Pecahan Mata Uang Rupiah yang paling Mungkin: ")

for p in pecahan:
    lembar = jumlah_uang // p
    jumlah_uang = jumlah_uang % p

    if lembar > 0:
        print(f"{lembar} lembar uang {p:,.0f} Rupiah.")
        