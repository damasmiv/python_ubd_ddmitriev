# Meminta input nilai A dari pengguna
a = int(input("Masukkan Nilai A = "))
# Meminta input nilai B dari pengguna
b = int(input("Masukkan Nilai B = "))
# Meminta input nilai C dari pengguna
c = int(input("Masukkan Nilai C = "))
# Membuat ekspresi-ekspresi logika
ekspresi1 = a + 4 < 10
ekspresi2 = b > a + 5
ekspresi3 = c - 3 >= 4
ekspresi4 = ekspresi1 or ekspresi2 or ekspresi3
# Menampilkan hasil ekspresi
print("\n")
print("Program Ekspresi OR")
print(f"Hasil dari ekspresi1 = a + 4 < 10 adalah {ekspresi1}")
print(f"Hasil dari ekspresi2 = b > a + 5 adalah {ekspresi2}")
print(f"Hasil dari ekspresi3 = c - 3 >= 4 adalah {ekspresi3}")
print(f"Hasil dari ekspresi4 = ekspresi1 or ekspresi2 or ekspresi 3 adalah {ekspresi4}")