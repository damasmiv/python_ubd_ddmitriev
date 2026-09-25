print("=============================")
print("Laporan Keuangan Bulanan Andi")
print("=============================")

kebutuhan_dasar = 60 / 100
rekreasi = 15 / 100
makan = 10 / 100
tabungan = 5 / 100
investasi = 10 / 100

gaji_andi = int(input("\nGaji Bulanan Andi: "))
print("\nPengeluaran:")
print(f"- Kebutuhan Dasar: Rp.{gaji_andi * kebutuhan_dasar:,.0f}")
print(f"- Rekreasi: Rp.{gaji_andi * rekreasi:,.0f}")
print(f"- Makan di Luar: Rp.{gaji_andi * makan:,.0f}\n")

total_pengeluaran = gaji_andi * kebutuhan_dasar + gaji_andi * rekreasi + gaji_andi * makan
print(f"Total Pengeluaran: Rp.{total_pengeluaran:,.0f}\n")

print(f"Tabungan: Rp.{gaji_andi * tabungan:,.0f}")
print(f"Investasi: Rp.{gaji_andi * investasi:,.0f}\n")
print("======================================================")



