#Loop Through a list
#Anda dapat melakukan pengulangan melalui item-item dalam daftar dengan menggunakan for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Loop Through the Index Numbers
#Gunakan fungsi range()dan len()untuk membuat iterable yang sesuai.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#Using a While Loop
#Anda dapat melakukan pengulangan pada item-item dalam daftar dengan menggunakan whileperulangan.
#Gunakan len()fungsi tersebut untuk menentukan panjang daftar, 
#lalu mulai dari 0 dan lakukan pengulangan melalui item daftar dengan merujuk ke indeksnya.
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#Looping Using List Comprehension
#Sebuah loop tangan pendek foryang akan mencetak semua item dalam daftar:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

