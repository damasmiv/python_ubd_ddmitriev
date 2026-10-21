print("Menu:")
print("1. Ulangi")
print("2. Keluar")
while True:
    userinput = int(input("Pilih Menu: "))
    if userinput == 1:
        print("Anda memilih menu 1.")
    elif userinput == 2:
        print("Anda memilih menu 2.")
        break
    else:
        print("Menu tidak tersedia, silakan pilih menu 1 atau 2.")
