'''List adalah salah satu dari 4 tipe data bawaan dalam Python yang digunakan untuk menyimpan kumpulan data,
3 lainnya adalah Tuple , Set , dan Dictionary , semuanya dengan kualitas dan penggunaan yang berbeda.'
'''
#List
thislist = ["apple", "banana", "cherry"]
print(thislist) #Output: ['apple', 'banana', 'cherry']
print("\n")

#List Items
'''
Item dalam daftar diurutkan, dapat diubah, dan memperbolehkan nilai duplikat.
Item daftar diindeks, item pertama memiliki indeks [0], item kedua memiliki indeks, [1]dan seterusnya.
'''

#Ordered
'''
Ketika kita mengatakan bahwa daftar diurutkan, artinya item-itemnya memiliki urutan yang pasti, dan urutan itu tidak akan berubah.
Jika Anda menambahkan item baru ke suatu daftar, item baru tersebut akan ditempatkan di akhir daftar.'
'''

#Note: Ada beberapa List methods yang akan mengubah urutan, tetapi secara umum: urutan item tidak akan berubah.

#Changesable
''''
List tersebut dapat diubah, artinya kita dapat mengubah, menambah, dan menghapus item dalam daftar setelah daftar dibuat.'
'''

#Allow Duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist) #Output: ['apple', 'banana', 'cherry', 'apple', 'cherry']

#List Length
#Untuk mengetahui berapa banyak item dalam daftar, Anda dapat menggunakan fungsi len()'
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) #Output: 3

#List Items - Data Types
list1 = ["apple", "banana", "cherry"] #list of string
list2 = [1, 5, 7, 9, 3] #list of int
list3 = [True, False, False] #list of boolean

# Suatu daftar dapat berisi berbagai tipe data:
list1 = ["abc", #string
         34, #int
         True,] #boolean
print(list1) #Output: ['abc', 34, True]

#type()
#Dapatkan tipe data dari daftar
mylist = ["apple", "banana", "cherry"]
print(type(mylist)) #Output: <class 'list'>

#The list() Constructor
#Ini juga mungkin untuk menggunakan konstruktor list() untuk membuat daftar
thislist = list(("apple", "banana", "cherry")) #note the double round-brackets
print(thislist) #Output: ['apple', 'banana', 'cherry']

''''
Koleksi Python (Array)
Ada empat tipe data koleksi dalam bahasa pemrograman Python:
- List adalah koleksi yang diurutkan dan dapat diubah. Mengizinkan anggota duplikat.
- Tuple adalah koleksi yang teratur dan tidak dapat diubah. Mengizinkan anggota duplikat.
- Set adalah koleksi yang tidak berurutan, tidak dapat diubah*, dan tidak terindeks. Tidak ada anggota yang duplikat.
- Dictionary adalah koleksi yang teratur** dan dapat diubah. Tidak ada anggota yang duplikat.
Saat memilih jenis koleksi, penting untuk memahami properti jenis tersebut. 
Memilih jenis yang tepat untuk kumpulan data tertentu dapat berarti mempertahankan makna, 
dan dapat berarti peningkatan efisiensi atau keamanan.
'''