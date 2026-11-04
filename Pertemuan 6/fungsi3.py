def hitung_diskon(pembelian):
    if pembelian >= 100000:
        diskon = pembelian * 0.1
    elif pembelian >= 50000:
        diskon = pembelian * 0.05
    else:
        diskon = 0
    return diskon
pembelian = int(input("Masukkan total pembelian: "))
diskon = hitung_diskon(pembelian)
print(f"Anda mendapatkan diskon sebesar Rp {diskon:,.0f}")