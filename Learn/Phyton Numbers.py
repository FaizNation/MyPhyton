#Ada tiga tipe numerik dalam Python:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#Untuk memverifikasi tipe data dari setiap variabel, Anda dapat menggunakan fungsi type().
print(type(x))
print(type(y))
print(type(z))

print("====================================")
#Int/integers adalah bilangan bulat positif atau negatif tanpa desimal tanpa batas
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

print("====================================")
#Float/float adalah bilangan positif atau negatif dengan satu atau lebih desimal
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#Float juga bisa berupa angka ilmiah dengan "e" untuk menunjukkan pangkat 10.
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

print("====================================")
#Complex/complex adalah bilangan imajiner "j"
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

print("====================================")
#Anda dapat mengonversi dari satu tipe ke tipe lain dengan metode int(), float(), dan complex():
#example
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
#Note: Anda tidak dapat mengonversi angka kompleks menjadi angka lain.

print("====================================")
#Python tidak memiliki random()fungsi untuk membuat angka acak, 
#tetapi Python memiliki modul bawaan yang disebut 'random' yang dapat digunakan untuk membuat angka acak:
import random

print(random.randrange(1, 10))


