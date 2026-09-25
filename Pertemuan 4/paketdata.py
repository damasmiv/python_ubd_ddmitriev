


print("========================")
print("Program Harga Paket Data")
print("========================")
print("Pilihan Operator (Kode)")
print("- T: Telkomsel\n- I: Indosat\n- X: XL Axiata")



harga_a_t = 30000
harga_b_t = 50000
harga_c_t = 90000

harga_a_i = 25000
harga_b_i = 45000
harga_c_i = 80000

harga_a_x = 28000
harga_b_x = 43000
harga_c_x = 85000



while True:
    userInput = input("\nMasukkan Kode Operator: ").upper()
    if userInput == "T":
        nama_operator = "Telkomsel"
        print("\nPiihan Besaran Paket (Kode)")
        print("- A: 2GB\n- B: 5GB\n- C: 10GB")
        break
    elif userInput == "I":
        nama_operator = "Indosat"
        print("\nPiihan Besaran Paket (Kode)")
        print("- A: 2GB\n- B: 5GB\n- C: 10GB")
        break
    elif userInput == "X":
        nama_operator = "XL Axiata"
        print("\nPiihan Besaran Paket (Kode)")
        print("- A: 2GB\n- B: 5GB\n- C: 10GB")
        break
    else:
        print("Kode Tidak Ditemukan! silahkan masukkan kode yang benar")

while True:
    paketdata = input("\nMasukkan Kode Besaran Paket: ").upper()
    if paketdata == "A":
        besaran_paket = "2GB"
        break
    elif paketdata == "B":
        besaran_paket = "5GB"
        break
    elif paketdata == "C":
        besaran_paket = "10GB"
        break
    else:
        print("Kode Tidak Sesuai! silahkan masukkan kode yang benar")

# PENENTU HARGA
harga_satuan = 0
if userInput == "T":
    if paketdata == "A":
        harga_satuan = harga_a_t
    elif paketdata == "B": 
        harga_satuan = harga_b_t
    elif paketdata == "C": 
        harga_satuan = harga_c_t

if userInput == "I":
    if paketdata == "A":
        harga_satuan = harga_a_i
    elif paketdata == "B": 
        harga_satuan = harga_b_i
    elif paketdata == "C": 
        harga_satuan = harga_c_i

if userInput == "X":
    if paketdata == "A":
        harga_satuan = harga_a_x
    elif paketdata == "B": 
        harga_satuan = harga_b_x
    elif paketdata == "C": 
        harga_satuan = harga_c_x

jumlah_paket = int(input("Masukkan Jumlah Pembelian (dalam jumlah paket): "))

total_harga = harga_satuan * jumlah_paket

print("\nInformasi Paket data yang Dibeli:")
print("Operator: ",nama_operator)
print("Besaran Paket: ",besaran_paket) 
print("Jumlah pembelian paket: ",jumlah_paket)
print(f"Total Harga: Rp.{total_harga:,.0f}")