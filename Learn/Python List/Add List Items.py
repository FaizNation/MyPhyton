#Append Items
#Untuk menambahkan item di akhir daftar, gunakan metode append() .
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) #Output: ['apple', 'banana', 'cherry', 'orange']

#Insert Items
#Untuk menambahkan item di posisi tertentu, gunakan metode insert() .
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) #Output: ['apple', 'orange', 'banana', 'cherry']

#Extend List
#Untuk menambahkan elemen dari daftar lain ke daftar saat ini, gunakan metode extend() .
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) #Output: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

#Add Any Iterable
#Metode extend() tidak harus menambahkan daftar, Anda dapat menambahkan elemen dari tupel, set, dictionary, atau daftar lain.
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) #Output: ['apple', 'banana', 'cherry', 'kiwi', 'orange']