jumlahbaris = int(input("Masukkan jumlah baris: "))
for i in range(1, jumlahbaris + 1):
    total = 0
    for j in range(1, i + 1):
        print(j, end=" ")
        total += j
        if j < i:
            print("+", end=" ")
    print(f"= {total}")