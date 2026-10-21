jumlahbaris = int(input("Masukkan jumlah baris: "))
for i in range(jumlahbaris, 0, -1):
    total = 1
    for j in range(i, 0, -1):
        angka = j * 2
        total *= angka
        print(angka, end=" ")
        if j> 1:
            print("*", end=" ")
    print(f"= {total}")

