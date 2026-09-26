print("====================================")
print("Kalkulator Pemasukan dan Pengeluaran")
print("====================================")

gaji = int(input("Masukkan Gaji Perjam yang anda inginkan: "))
jumlah_jam = int(input("Masukkan jumlah jam kerja dalam 1 minggu: "))

#LOGIC PERHITUNGAN
pendapatan = gaji * jumlah_jam
pajak = pendapatan * (14/100)
pendapatan_setelah_pajak = pendapatan - pajak
pakaian = pendapatan_setelah_pajak * (10/100)
alat_tulis = pendapatan_setelah_pajak * (1/100)
sisa_uang_setelah_belanja = pendapatan_setelah_pajak - pakaian - alat_tulis
sedekah = sisa_uang_setelah_belanja * (25/100)
yatim = sedekah * 30/100
dhuafa = sedekah - yatim

print(f"Pendapatan Budi selama libur musim panas sebelum Pajak: Rp.{pendapatan:,.0f}")
print(f"Pendapatan Budi selama libur musim panas setelah Pajak: Rp.{pendapatan_setelah_pajak:,.0f}")
print(f"Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris: Rp.{pakaian:,.0f}")
print(f"Jumlah uang yang akan Budi habiskan untuk membeli alat tulis: Rp.{alat_tulis:,.0f}")
print(f"Jumlah uang yang akan Budi sedekahkan: Rp.{sedekah:,.0f}")
print(f"Jumlah uang yang akan diterima anak yatim: Rp.{yatim:,.0f}")
print(f"Jumlah uang yang akan diterima dhuafa: Rp.{dhuafa:,.0f}")