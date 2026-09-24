print("==============================================")
print("Simulasi Menabung Rutin dengan Bunga Berbunga")
print("==============================================")

jumlah_awal = int(input("Masukkan Jumlah awal yang ingin ditabung (Dalam Rupiah): "))
bunga_tahunan = int(input("Masukkan Tingkat bunga Tahunan (Dalam Persentase): "))
periode_tabungan = int(input("Masukkan Periode Tabungan (dalam Tahun) "))
tabungan_rutin = int(input("Masukkan jumlah tabungan rutin per tahun (dalam Rupiah): "))

jumlah_akhir = jumlah_awal * (1 + bunga_tahunan / 100) ** periode_tabungan + (tabungan_rutin * periode_tabungan)

print(f"Setelah {periode_tabungan} tahun, jumlah uang yang akan anda Miliki adalah Rp.{jumlah_akhir:,.0f}")