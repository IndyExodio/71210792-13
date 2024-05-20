#KATEGORI APLIKASI DI PLAY STORE
#INPUT JUMLAH KATEGORI
n = int(input('Masukkan jumlah kategori: '))
#DICTIONARY KOSONG
data_aplikasi = {}
#INPUT NAMA KATEGORI DAN APLIKASINYA
for i in range(n):
    nama_kategori = input('Masukkan nama kategori:')
    print('Masukkan 5 nama kategori',nama_kategori)
    #LIST KOSONG UNTUK NAMA APLIKASI
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input('Nama aplikasi:')
        aplikasi.append(nama_aplikasi)
    #MASUKKAN DALAM DICTIONARY
    data_aplikasi[nama_kategori] = aplikasi
#TAMPILKAN DATA APLIKASI
print(data_aplikasi)

daftar_aplikasi_list = []
#AMBIL SEMUA DAFTAR APLIKASI DARI SETIAP KATEGORI
for aplikasi in data_aplikasi.values():
    daftar_aplikasi_list.append(set(aplikasi))
print(daftar_aplikasi_list)

#LAKUKAN INTERSECTION PADA SEMUA SET
hasil = daftar_aplikasi_list[0]
for i in range(1, len(daftar_aplikasi_list)):
    hasil = hasil.intersection(daftar_aplikasi_list[i])
print(hasil)

#LAKUKAN SYMMETRIC DIFFERENCE PADA SEMUA SET
hasil = daftar_aplikasi_list[0]
for i in range(1, len(daftar_aplikasi_list)):
    hasil = hasil.symmetric_difference(daftar_aplikasi_list[i])
print(hasil)

#JIKA JUMLAH N LEBIH DARI DUA MAKA AKAN DITAMPILKAN APLIKASI YANG MUNCUL PADA KEDUA KATEGORI
if n>2:
    for y in range(1,n):
        inter = daftar_aplikasi_list[i] & daftar_aplikasi_list[i-1]
    else:
        inter = daftar_aplikasi_list[0] & daftar_aplikasi_list[i]

    print('Aplikasi yang muncul di dua kategori sekaligus adalah ',inter)