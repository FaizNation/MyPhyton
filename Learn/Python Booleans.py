#Boolean Values
#example
print(10 > 9)
print(10 == 9)
print(10 < 9)

#Cetak pesan berdasarkan apakah kondisinya Trueatau False:
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Evaluate Values and Variables
#Fungsi ini bool()memungkinkan Anda untuk mengevaluasi nilai apa pun, dan memberi Anda Trueatau False sebagai gantinya,

#example string dan angka:
print(bool("Hello"))
print(bool(15))

#example Mengevaluasi dua variabel:
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#Most Values are True
'''
Hampir semua nilai dievaluasi Trueapakah memiliki semacam konten.
Semua string adalah True, kecuali string kosong.
Setiap bilangan adalah True, kecuali 0.
Semua daftar, tupel, himpunan, dan kamus adalah True, kecuali yang kosong.
'''
#example
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#Some Values are False
#Faktanya, tidak banyak nilai yang bernilai False,
#kecuali nilai kosong, seperti (), [], {}, "", angka 0, dan nilai None. Dan tentu saja nilainya Falsebernilai False.
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#Satu nilai lagi, atau objek dalam kasus ini, dievaluasi menjadi False,
#dan itu jika Anda memiliki objek yang dibuat dari kelas dengan __len__fungsi yang mengembalikan 0atau False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#Function can Return a Boolean
#example
def myFunction() :
  return True

print(myFunction())

#mengeksekusi kode berdasarkan jawaban Boolean suatu fungsi:
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#Python juga memiliki banyak fungsi bawaan yang mengembalikan nilai boolean,
#Seperti isinstance() fungsi, yang dapat digunakan untuk menentukan apakah suatu objek memiliki tipe data tertentu:
x = 200
print(isinstance(x, int))

