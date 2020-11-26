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



