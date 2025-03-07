#Banyak nilai ke beberapa variabel
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Note: Pastikan jumlah variabel sama dengan jumlah nilai

print("====================================")
#satukan nilai ke beberapa variabel
x = y = z = "Orange"
print(x)
print(y)
print(z)

print("====================================")
#Unpack a collection
'''
Jika Anda memiliki koleksi nilai dalam bentuk daftar, tuple, dll. 
Python memungkinkan Anda mengekstrak nilai ke dalam variabel yang berbeda.
'''
fruit = ["apple", "banana", "cherry"]
x, y, z = fruit
print(x) #output: apple
print(y) #output: banana
print(z) #output: cherry
