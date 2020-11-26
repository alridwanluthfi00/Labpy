# list bebas
a = [2, 4, 6, 8, 10]

# akses list
print(a[2]) # tampilkan elemen ke - 3

print(a[1:4]) # ambil nilai elemen ke - 2 sampai ke - 4

print(a[4]) # ambil elemen terakhir

print('==================================================')

# ubah elemen list
a[3] = 12 # ubah elemen ke 4 nilai lainnya
print(a)

a[3:5] = [11, 13] # ubah elemen ke 4 sampai dengan elemen terakhir
print(a)

print('==================================================')

# tambah elemen list
b = a [0:2] # ambil 2 bagian dari list pertama (A) dan jadikan list kedua (B)
print(b)

b.append('hai') # tambah list B dengan nilai string
print(b)

b.extend([16, 18, 20]) # tambah list B dengan 3 nilai
print(b)

x = a + b # gabungkan list B dengan list A
print(x)