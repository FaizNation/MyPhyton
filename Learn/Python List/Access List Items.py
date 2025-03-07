# list item dapat diakses dengan merujuk pada nomor indeks, dalam tanda kurung siku.
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) #Output: banana
print("\n")

#Note: Indeks pertama adalah 0.

#Negative Indexing
#Negative indexing berarti mulai dari akhir daftar
thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) #Output: cherry
print("\n")

#Range of Indexes
#Anda dapat menentukan rentang indeks dengan menentukan di mana untuk memulai dan di mana untuk akhir indeks.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #Output: ['cherry', 'orange', 'kiwi']
print("\n")
#Note: Pencarian akan dimulai pada indeks 2 (termasuk) dan berakhir pada indeks 5 (tidak termasuk).

#cara menghilangkan indeks pertama
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #Output: ['apple', 'banana', 'cherry', 'orange']
print("\n")

#cara menghilangkan indeks terakhir
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) #Output: ['cherry', 'orange', 'kiwi', 'melon', 'mango']

#Range of Negative Indexes
#tentukan indeks negatif
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #Output: ['orange', 'kiwi', 'melon']
print("\n")

#Check if Item Exists
#Untuk menentukan apakah item tertentu ada dalam daftar Python, gunakan in keyword.
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list") #Output: Yes, 'apple' is in the fruits list