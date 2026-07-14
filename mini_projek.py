# KALKULATOR STRUK BELANJA SEDERHANA

barang1 = 'Kopi'
harga_barang1 = 15000
barang2 = 'Teh'
harga_barang2 = 10000

print('Daftar Menu')
print('=============')
print(barang1, '=', harga_barang1)
print(barang2, '=', harga_barang2)
print()

isi = input('Masukkan nama barang yang ingin dibeli: ')
jum = int(input('Masukkan jumlah barang yang ingin dibeli: '))

harga_satuan = harga_barang1 if isi.lower() == barang1.lower() else harga_barang2 if isi.lower() == barang2.lower() else 0

subtotal = harga_satuan * jum

diskon = 10 if subtotal >= 20000 else 0
nilai_diskon = subtotal * diskon / 100
setelah_diskon = subtotal - nilai_diskon

print('=== STRUK BELANJA ===')
print('Barang       :', isi)
print('Harga satuan :', harga_satuan)
print('Jumlah       :', jum)
print('Subtotal     :', subtotal)
print('Diskon (' + str(diskon) + '%) :', nilai_diskon)
print('Total bayar  :', setelah_diskon)
