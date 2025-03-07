#Remove specified item
#Untuk menghapus item tertentu, gunakan metode remove() .
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) #Output: ['apple', 'cherry']

#jika ada lebih dari satu item yang cocok, hanya item pertama yang akan dihapus
thislist = ["apple", "banana", "cherry", "apple"]
thislist.remove("apple")
print(thislist) #Output: ['banana', 'cherry', 'apple']

#Remove specified index
#Untuk menghapus item pada indeks tertentu, gunakan metode pop() .
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) #Output: ['apple', 'cherry']

#jika Anda tidak menentukan indeks, metode pop() menghapus item terakhir.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) #Output: ['apple', 'banana']

#The del keyword
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) #Output: ['banana', 'cherry']

#The del keyword juga dapat menghapus daftar sepenuhnya
thislist = ["apple", "banana", "cherry"]
del thislist


#The clear() method
#Untuk mengosongkan daftar, gunakan metode clear() .
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) 



