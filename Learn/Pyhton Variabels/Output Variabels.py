#Fungsi pyhton print() digunakan untuk menampilkan output ke layar

#example
x = "Pyhton is awesome"
print(x) #output: Pyhton is awesome

print("====================================")
#Dalam print() fungsi tersebut, kita mengeluarkan beberapa variabel, dipisahkan koma
#example
x = "Python"
y = "is"
z = "awesome"
print(x, y, z) #output: Phython is awesome

print
#Kita juga dapat menggunakan operator + 
#example
x = "Python"
y = "is"
z = "awesome"
print (x + y + z)

#Note:Perhatikan karakter spasi setelah "Python "dan "is ", tanpa keduanya hasilnya akan menjadi "Pythonisawesome".

print("====================================")
#Untuk angka, +karakter tersebut berfungsi sebagai operator matematika:
x = 5
y = 10
print(x + y)

print
#tidak bisa menggabungkan string dengan int
x = 5
y = "John"
print(x + y)

print("====================================")
#untuk menampilkan beberapa variabel dalam print()fungsi adalah dengan memisahkannya dengan koma.
x = 5
y = "John"
print(x, y)