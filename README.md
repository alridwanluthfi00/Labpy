# Lab 4
## Latihan 

![1](https://user-images.githubusercontent.com/73066008/100188881-bf998b00-2f1d-11eb-8ca2-18b4264fcd2c.png)

__Input code__ :

![3](https://user-images.githubusercontent.com/73066008/100225178-63039380-2f50-11eb-8028-1360fb30acc0.png)
   
![4](https://user-images.githubusercontent.com/73066008/100225217-7151af80-2f50-11eb-96fc-96b4efacdc67.png)

__Penjelasan__ :

* a = [2, 4, 6, 8, 10] ( list a dengan 5 elemen )

_Akses list_

* print(a[2]) menampilkan elemen ke - 3
* print(a[1:4]) mengambil nilai elemen ke 2 sampai elemen ke 4
* print(a[4]) mengambil elemen terakhir

_Ubah elemen list_

* a[3] = 12 mengubah elemen ke 4 dengan nilai lainnya
* a[3:5] = [11, 13] mengubah elemen ke 4 sampai dengan elemen terakhir

_Tambah elemen list_

* b = a [0:2] mengambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
* b.append('hai') menambah list B dengan nilai string
* b.extend([16, 18, 20]) menambah list B dengan 3 nilai
* x = a + b menggabungkan list B dengan list A

__Output code__ :

![5](https://user-images.githubusercontent.com/73066008/100229061-3ce0f200-2f56-11eb-97e5-53569f5b7cc3.png)

## Tugas Praktikum 4

![2](https://user-images.githubusercontent.com/73066008/100228876-f095b200-2f55-11eb-94fd-503c31523a03.png)

__Input code__ :

![6](https://user-images.githubusercontent.com/73066008/100290868-e81d9580-2fae-11eb-953c-9c998c1b1498.png)

__Penjelasan__ :

* data = [] Membuat list kosong yang nanti akan di isi
* while ulangi =='y': Membuat perulangan dengan variabel ulangi, dimana ketika memilih 'y' maka akan otomatis mengulang pengisian data
* nilai_akhir = (nilai_tugas)*30/100 + (nilai_uts)*35/100 + (nilai_uas)*35/100 Nilai Akhir diambil dari perhitungan 3 komponen nilai (tugas: 30%, uts: 35%, uas: 35%)
* data.append([nama, nim, nilai_tugas, nilai_uts, nilai_uas, int(nilai_akhir)]) Memasukkan variabel input ke dalam list data
* ulangi = (input('tambah data?(y/t)')) Ketika memilih 't' if ulangi == 't': maka cetaklah hasil

__Output code__ :

![7](https://user-images.githubusercontent.com/73066008/100290888-f2d82a80-2fae-11eb-8036-07ae24ac5dad.png)

__Flowchart__ :

![8](https://user-images.githubusercontent.com/73066008/100294630-fa510100-2fb9-11eb-8f7b-ab4d0b9dc200.png)

# Lab 5
## Tugas Praktikum 5

![9](https://user-images.githubusercontent.com/73066008/100308112-20869900-2fda-11eb-8ee4-e7f22b11f4f7.png)

__Input code__ :

![10](https://user-images.githubusercontent.com/73066008/100311201-cf7aa300-2fe1-11eb-96ff-7174d88d23e2.png)

![11](https://user-images.githubusercontent.com/73066008/100311223-d73a4780-2fe1-11eb-8336-5013bdd4165d.png)

![12](https://user-images.githubusercontent.com/73066008/100311232-df928280-2fe1-11eb-95f6-fcb324a57a03.png)

![13](https://user-images.githubusercontent.com/73066008/100311241-e5886380-2fe1-11eb-8385-dd714ee5b9a2.png)

![14](https://user-images.githubusercontent.com/73066008/100311255-ed480800-2fe1-11eb-9c59-321a0a4c25c7.png)

__Penjelasan__ :

_Header_

* data={} untuk menampung list dengan format dictionary
* Gunakanlah perulangan While untuk menampilkan data sebanyak banyaknya
* menu = input("(T)ambah, (U)bah, (H)apus, (L)ihat, (C)ari, (K)eluar: ") kita tambahkan input Tambah, Ubah, Hapus, Lihat, Cari, Keluar dalam variabel menu
* else: print("Upss ada yang salah, silahkan cek kembali.") jika kita salah dalam input maka akan tercetak 'silahkan cek kembali.'
* masukan nama, nim, nilai_tugas, nilai_uts, nilai_uas, dan nilai_akhir yang nanti akan di masukkan kedalam data={}
* Nilai akhir didapat dari = (nilai_tugas)*30/100 + (nilai_uts)*35/100 + (nilai_uas)*35/100

_Lihat data_

* elif menu.lower() == 'l': Kita menggunakan kondisi percabangan if, ambil data dari menu lalu kita akan mengubah perintah 'l' yang kita input menjadi huruf kecil dengan fungsi lower()
* lalu cetak print()

_Tambah data_

* elif menu.lower() == 't': Ambil data 't' dari menu
* nama = input("Masukan nama: ") lalu tambahkan input nama, nim, nilai tugas, uts, uas
* nilai_akhir = (nilai_tugas)*30/100 + (nilai_uts)*35/100 + (nilai_uas)*35/100 untuk nilai akhir diambil dari perhitungan 3 komponen nilai (nilai_tugas: 30%, nilai_uts: 35%, * nilai_uas: 35%)
*data[nama] = [nama, nim, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir] kita akan masukkan data yang tadi kita input ke dalam `data[nama]'
* lalu cetak print()

_Ubah data_

* elif menu.lower() == 'u': Ambil data 'u' dari menu
* nama = input("Masukan nama untuk mengubah data: ") kita akan menginput data yang nanti akan di ubah
* if nama in data.keys(): print("Ingin mengubah apa?") jika 'nama' dari di dalam 'data' maka akan mengembalikan daftar menggunakan fungsi 'keys()' lalu di cetak lah 'print()'
sub_data = input("(Semua), (Nama), (NIM), (Tugas), (UTS), (UAS) : ") membuat menu ubah di dalam sub_data
* if sub_data.lower() == "semua": ambil kata kunci 'semua' di dalam sub_data jika 'semua' maka input data[nama][1] = input("Ubah NIM:") data[nama][2] = int(input("Ubah Nilai Tugas: ")) data[nama][3] = int(input("Ubah Nilai UTS: ")) data[nama][4] = int(input("Ubah Nilai UAS: "))
*data[nama][5] = data[nama][2] *30/100 + data[nama][3]*35/100 + data[nama][4] *35/100 kita dapatkan nilai akhir dengan diambil dari perhitungan 3 komponen nilai (tugas: 30%, uts: 35%, uas: 35%),ket: [5] = nilai_akhir, dimana [0] = nama
* lalu cetak print("\nBerhasil ubah data!")
* Jika kita ingin mengubah data tertentu maka elif sub_data.lower() == "nim": data[nama][1] = input("NIM:") dan berlaku juga untuk nilai tugas, UTS dan UAS
* lalu cetak print("\nBerhasil ubah data!")
* else: print("'{}' tidak ditemukan.".format(nama)) jika kita salah dalam memasukkan nama untuk mengubah data maka akan muncul 'nama tidak di temukan'

_Hapus data_

* elif menu.lower() == 'h': Ambil data 'h' dari menu
* nama = input("Masukan nama untuk menghapus data : ") kita akan menginput data yang nanti akan di hapus
* if nama in data.keys(): kita mengambil list 'nama' di dalam 'data' menggunakan pengkondisian
* del data[nama] hapus semua 'nama' yang ada di dalam 'data'
* jika sudah maka cetak print("sub_data '{}' berhasil dihapus.".format(nama))
* else: print("'{}' tidak ditemukan.".format(nama)) jika data yang kita input salah/tidak ditemukan maka akan tercetak 'nama tidak di temukan'

_Cari data_

* elif menu.lower() == 'c': Ambil data 'c' dari menu
* nama = input("Masukan nama untuk mencari data: ") kita akan menginput data yang nanti akan di cari
* if nama in data.keys(): kita mengambil list 'nama' di dalam 'data' menggunakan pengkondisian
* maka cetak print("Nama: {0}\nNIM : {1}\nNilai Tugas: {2}\nUTS: {3}\nUAS: {4}\nNilai akhir: {5}" untuk menampilkan data yang tersedia
* else: print("'{}' tidak ditemukan.".format(nama)) jika data yang kita input salah/tidak ditemukan maka akan tercetak 'nama tidak di temukan'

_Keluar_

* if menu.lower() == 'k': Ambil data 'k' dari menu
* lalu break untuk menghentikan seluruh proses



__Output code__ :



