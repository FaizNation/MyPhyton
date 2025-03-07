#Change item value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) #Output: ['apple', 'blackcurrant', 'cherry']

#Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) #Output: ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango'] 
 
#jika Anda memasukkan lebih banyak elemen daripada yang Anda ganti, elemen baru akan dimasukkan di posisi yang ditentukan
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) #Output: ['apple', 'blackcurrant', 'watermelon', 'cherry']  
#Note: Jumlah elemen yang dimasukkan tidak harus sama dengan jumlah elemen yang diganti.

#jika Anda memasukkan lebih sedikit elemen daripada yang Anda ganti, elemen yang tersisa akan bergeser ke kiri
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) #Output: ['apple', 'watermelon']

#Insert Items
#Untuk menambahkan item di posisi tertentu, gunakan metode insert() .
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) #Output: ['apple', 'banana', 'watermelon', 'cherry']
#Note: sebagai hasil, list akan berisi 4 item.