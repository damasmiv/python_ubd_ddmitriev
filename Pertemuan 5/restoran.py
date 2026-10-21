print("Selamat datang di Restoran UBD!")

#MENU SECTION
print("Menu Makanan:")
print("1. Nasi Goreng - Rp 20.000")
print("2. Mie Ayam - Rp 15.000")
print("3. Ayam Bakar - Rp 25.000")
print("4. Sate - Rp 30.000\n")

print("Menu Minuman:")
print("1. Teh Manis - Rp 5.000")
print("2. Es Jeruk - Rp 7.000")
print("3. Kopi Hitam - Rp 8.000")
print("4. Air Mineral - Rp 3.000\n")

#INPUT SECTION
while True:
    while True:
        userinput = int(input("Masukkan Menu Makanan 1-4: "))
        if userinput == 1:
            harga = 20000
            pesanan = "Nasi Goreng"
            break
       
        elif userinput == 2:
            harga = 15000
            pesanan = "Mie Ayam"
            break
        
        elif userinput == 3:
            harga = 25000
            pesanan = "Ayam Bakar"
            break
        
        elif userinput == 4:
            harga = 30000
            pesanan = "Sate"
            break
        
        else:
            print("Menu tidak tersedia, silakan pilih menu 1-4.")
        
    while True:
        userinput2 = int(input("Masukkan Menu Minuman 1-4: "))
        if userinput2 == 1:
            harga2 = 5000
            pesanan2 = "Teh Manis"
            break
        elif userinput2 == 2:
            harga2 = 7000
            pesanan2 = "Es Jeruk"
            break
        elif userinput2 == 3:
            harga2 = 8000
            pesanan2 = "Kopi Hitam"
            break
        elif userinput2 == 4:
            harga2 = 3000
            pesanan2 = "Air Mineral"
            break
        else:
            print("Menu tidak tersedia, silakan pilih menu 1-4.")
        

#LOGIC PERHITUNGAN
    totalharga = harga + harga2
    print("\nPesanan Anda\n")
    print(f"- {pesanan} - Rp {harga:,.0f}")
    print(f"- {pesanan2} - Rp {harga2:,.0f}")
    print(f"Total Harga: Rp {totalharga:,.0f}")

    lanjut = input("\nTerima kasih telah berkunjung ke Restoran UBD, apakah anda ingin memesan lagi? (Y/N)")
    if lanjut.lower() != "y":
        print("Terima kasih telah berbelanja di Restoran UBD!")
        break
    
