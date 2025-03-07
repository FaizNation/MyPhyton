'''
Mungkin ada saatnya Anda ingin menentukan tipe pada variabel. Ini dapat dilakukan dengan casting. 
Python adalah bahasa berorientasi objek, 
dan karenanya menggunakan kelas untuk menentukan tipe data, termasuk tipe primitifnya.
Oleh karena itu, casting dalam python dilakukan dengan menggunakan fungsi konstruktor:

1. int() - membuat bilangan integer dari literal integer, literal float (dengan menghilangkan semua desimal), atau literal string (dengan syarat string mewakili bilangan bulat)
2. float() - membuat bilangan float dari literal integer, literal float, atau literal string (dengan syarat string tersebut mewakili float atau integer)
3. str() - membuat string dari berbagai macam tipe data, termasuk string, literal integer, dan literal float
'''

#example integers
x = int(1) # x akan menjadi 1
y = int(2.8) # y akan menjadi 2
z = int("3") # z akan menjadi 3

#example float
x = float(1) # x akan menjadi 1.0
y = float(2.8) # y akan menjadi 2.8
z = float("3") # z akan menjadi 3.0
w = float("4.2") # w akan menjadi 4.2

#example string
x = str("s1") # x akan menjadi 's1'
y = str(2) # y akan menjadi '2'
z = str(3.0) # z akan menjadi '3.0'