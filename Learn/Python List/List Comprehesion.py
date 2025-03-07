#Berdasarkan daftar buah-buahan, Anda menginginkan daftar baru yang hanya berisi buah-buahan dengan huruf "a" dalam namanya.
#Tanpa pemahaman daftar, Anda harus menulis forpernyataan dengan pengujian kondisional di dalamnya:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#Dengan List Comprehesion, Anda dapat melakukan semua itu hanya dengan satu baris kode:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#The syntax
# newlist = [expression for item in iterable if condition == True]

#Condition
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)

# Kondisi if x != "apple"  akan kembali Trueuntuk semua elemen selain "apel", membuat daftar baru berisi semua buah kecuali "apel".
# Kondisi ini bersifat opsional dan dapat dihilangkan:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits]

print(newlist)

# Iterable
# Anda dapat menggunakan range()fungsi ini untuk membuat sesuatu yang dapat diulang:
newlist = [x for x in range(10)]

print(newlist)

# Contoh yang sama, tetapi dengan suatu kondisi
newlist = [x for x in range(10) if x < 5]

print(newlist)

# Expression
# Tetapkan nilai dalam daftar baru ke huruf besar:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)

# Anda dapat mengatur hasil sesuai keinginan Anda:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)

# Ekspresi tersebut juga dapat berisi kondisi, bukan seperti filter, tetapi sebagai cara untuk memanipulasi hasilnya:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)
