print("================================================")
print("Mesin Waktu Tabungan Rutin dengan Bunga Berbunga")
print("================================================")


jumlah_awal = int(input("Masukkan Jumlah awal yang ingin ditabung (Dalam Rupiah): "))
bunga_tahunan = int(input("Masukkan Tingkat bunga Tahunan (Dalam Persentase): "))
periode_tabungan = int(input("Masukkan Periode Tabungan (dalam Tahun): "))
tabungan_rutin = int(input("Masukkan jumlah tabungan rutin per tahun (dalam Rupiah): "))

jumlah_akhir = jumlah_awal * (1 + bunga_tahunan / 100) ** periode_tabungan + (tabungan_rutin * periode_tabungan)


total_profit = jumlah_akhir - jumlah_awal
roi = (total_profit / jumlah_awal) * 100
total_setoran = tabungan_rutin + (tabungan_rutin * periode_tabungan)
total_bunga_majemuk = jumlah_akhir - total_setoran

print("==========================================================================================================")
print(f"Setelah {periode_tabungan} tahun, jumlah uang yang akan anda miliki adalah Rp.{jumlah_akhir:,.0f}")
print("==========================================================================================================")
print("Dengan rincian sebagai berikut")
print(f"Jumlah setoran awal: Rp.{jumlah_awal:,.0f}")
print(f"Jumlah total saldo: Rp.{jumlah_akhir:,.0f}")
print(f"Jumlah total setoran: Rp.{total_setoran:,.0f}")
print(f"ROI (Return of Investment): {roi:.2f}%")
print(f"Total bunga majemuk yang diperoleh: + Rp.{total_bunga_majemuk:,.0f}")

