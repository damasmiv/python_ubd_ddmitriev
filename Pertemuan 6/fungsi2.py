def hitung_tagihan_listrik(jumlah_pemakaian, golongan_tarif=3):
    if golongan_tarif == 1:
        harga_100kwh_pertama = 1500
        harga_setelah_100kwh = 2000
    elif golongan_tarif == 2:
        harga_100kwh_pertama = 2500
        harga_setelah_100kwh = 3000
    elif golongan_tarif == 3:
        harga_100kwh_pertama = 4000
        harga_setelah_100kwh = 5000
    elif golongan_tarif == 4:
        harga_100kwh_pertama = 5000
        harga_setelah_100kwh = 7000
    else:
        return "Golongan tarif tidak valid"
    if jumlah_pemakaian <= 100:
        total_tagihan = jumlah_pemakaian * harga_100kwh_pertama
    else:
        total_tagihan = (100 * harga_100kwh_pertama) + ((jumlah_pemakaian - 100) * harga_setelah_100kwh)
    return total_tagihan
# Contoh penggunaan fungsi jika pemakaian sebesar 150 kwh dan Golongan tarif 2
tagihan = hitung_tagihan_listrik(150, 2)
print(f"Tagihan listrik anda adalah: Rp. {tagihan}")
# Contoh penggunaan fungsi jika pemakaian sebesar 80 kwh dan Golongan tarif 3
tagihan = hitung_tagihan_listrik(80, 3)
print(f"Tagihan listrik anda adalah: Rp. {tagihan}")