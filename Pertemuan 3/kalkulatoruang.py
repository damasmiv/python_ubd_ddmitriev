print("===================================")
print("Kalkulator Susunan Mata Uang Rupiah")
print("===================================")
jumlah_uang = int(input("Masukkan Jumlah Uang Ali: "))

print("Jumlah Uang Ali: ", jumlah_uang)

#LOGIC
lembar_100k = jumlah_uang // 100000
sisa_uang = jumlah_uang % 100000

lembar_50k = sisa_uang // 50000
sisa_uang = sisa_uang % 50000

lembar_20k = sisa_uang // 20000
sisa_uang = sisa_uang % 20000

lembar_10k = sisa_uang // 10000
sisa_uang = sisa_uang % 10000

lembar_5k = sisa_uang // 5000
sisa_uang = sisa_uang % 5000

lembar_2k = sisa_uang // 2000
sisa_uang = sisa_uang % 2000

lembar_1k = sisa_uang // 1000
sisa_uang = sisa_uang % 1000

koin_500 = sisa_uang // 500
sisa_uang = sisa_uang % 500

koin_200 = sisa_uang // 200
sisa_uang = sisa_uang % 200

koin_100 = sisa_uang // 100
sisa_uang = sisa_uang % 100

print("Kombinasi Pecahan Mata Uang Rupiah yang paling Mungkin: ")

if lembar_100k > 0:
    print(f"{lembar_100k} lembar uang kertas 100,000 Rupiah")

if lembar_50k > 0:
    print(f"{lembar_50k} lembar uang kertas 50,000 Rupiah")

if lembar_20k > 0:
    print(f"{lembar_20k} lembar uang kertas 20,000 Rupiah")

if lembar_10k > 0:
    print(f"{lembar_10k} lembar uang kertas 10,000 Rupiah")

if lembar_5k > 0:
    print(f"{lembar_5k} lembar uang kertas 5,000 Rupiah")

if lembar_2k > 0:
    print(f"{lembar_2k} lembar uang kertas 2,000 Rupiah")

if lembar_1k > 0:
    print(f"{lembar_1k} lembar uang kertas 1,000 Rupiah")

if koin_500 > 0:
    print(f"{koin_500} uang koin 500 Rupiah")

if koin_200 > 0:
    print(f"{koin_200} uang koin 200 Rupiah")

if koin_100 > 0:
    print(f"{koin_100} uang koin 100 Rupiah")