#Operator digunakan untuk melakukan operasi pada variabel dan nilai.
print (10 + 5) #penjumlahan

'''
Python membagi operator ke dalam kelompok berikut:
- Operator Aritmatika
- Operator penugasan
- Operator perbandingan
- Operator logika
- Operator identitas
- Operator keanggotaan
- Operator bitwise
'''

#Operator Aritmatika
##Addition
x = 10
y = 5
print(x + y) #Output: 15

##Subtraction
x = 10
y = 5
print(x - y) #Output: 5

##Multiplication
x = 10
y = 5
print(x * y) #Output: 50

##Division
x = 10
y = 5
print(x / y) #Output: 2.0

##Modulus
x = 10
y = 3
print(x % y) #Output: 1

##Exponentiation
x = 10
y = 3
print(x ** y) #Output: 1000

##Floor division
x = 10
y = 3
print(x // y) #Output: 3

print("\n")

#Operator Penugasan
##Operator penugasan digunakan untuk menetapkan nilai ke variabel.

# =
x = 5
print(x) #Output: 5

# +=
x = 5
x += 3
print(x) #Output: 8

# -=
x = 5
x -= 3
print(x) #Output: 2

# *=
x = 5
x *= 3
print(x) #Output: 15

# /=
x = 5
x /= 3
print(x) #Output: 1.6666666666666667

# %=
x = 5
x %= 3
print(x) #Output: 2

# //=
x = 5
x //= 3
print(x) #Output: 1

# **=
x = 5
x **= 3
print(x) #Output: 125

# &=
x = 5
x &= 3
print(x) #Output: 1

# |=
x = 5
x |= 3
print(x) #Output: 7

# ^=
x = 5
x ^= 3
print(x) #Output: 6

# >>=
x = 5
x >>= 3
print(x) #Output: 0 

# <<=
x = 5
x <<= 3
print(x) #Output: 40

#:=
print(x := 3) #Output: 5

print("\n")

#Operator Perbandingan
##Operator perbandingan digunakan untuk membandingkan dua nilai.

# == (Equal)
x = 5
y = 3
print(x == y) #Output: False

# != (Not Equal)
x = 5
y = 3
print(x != y) #Output: True

# > (Greater than)
x = 5
y = 3
print(x > y) #Output: True

# < (Less than)
x = 5
y = 3
print(x < y) #Output: False

# >= (Greater than or equal to)
x = 5
y = 3
print(x >= y) #Output: True

# <= (Less than or equal to)
x = 5
y = 3
print(x <= y) #Output: False

print("\n")

#Operator Logika
##Operator logika digunakan untuk menggabungkan pernyataan bersyarat(conitional statement).

# and 
x = 5
print(x > 3 and x < 10) #Output: True
# retrun True karena 5 lebih besar dari 3 dan 5 lebih kecil dari 10

# or
x = 5
print(x > 3 or x < 4) #Output: True

# not
x = 5
print(not(x > 3 and x < 10)) #Output: False
# return False karena tidak ada pernyataan yang salah

print("\n")

#Operator Identitas
##Operator identitas digunakan untuk membandingkan objek, 
#bukan jika mereka sama, tetapi jika mereka sebenarnya sama objek, dengan membandingkan lokasi memori.

# is
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) #Output: True
# return True karena x adalah objek yang sama dengan z
print(x is y) #Output: False
# return False karena x bukan objek yang sama dengan y, meskipun mereka memiliki konten yang sama
print(x == y) #Output: True
# untuk menujukan perbedaan antara "is" dan "==", 
# perbandingan ini mengembalikan True karena x adalah objek yang sama dengan y

# is not
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z) #Output: False
# return False karena x adalah objek yang sama dengan z
print(x is not y) #Output: True
# return True karena x bukan objek yang sama dengan y
print(x != y) #Output: False
# untuk menujukan perbedaan antara "is not" dan "!=",

print("\n")

#Operator Keanggotaan
##Operator keanggotaan digunakan untuk menguji apakah urutan disajikan dalam objek.

# in
x = ["apple", "banana"]
print("banana" in x) #Output: True
# return True karena objek "banana" ada dalam list

# not in
x = ["apple", "banana"]
print("pineapple" not in x) #Output: True
# return True karena objek "pineapple" tidak ada dalam list

print("\n")

#Operator Bitwise
##Operator bitwise digunakan untuk membandingkan angka (biner).

# & (AND)
print(6 & 3) #Output: 2
'''
Operator & membandingkan setiap bit dan menetapkannya ke 1 jika keduanya bernilai 1, jika tidak, ditetapkan ke 0:

6 = 00000000000000110
3 = 00000000000000011
--------------------
2 = 00000000000000010
====================

Angka desimal dan nilai binernya:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
'''

# | (OR)
print(6 | 3) #Output: 7
''''
Operator | membandingkan setiap bit dan menetapkannya ke 1 jika satu atau keduanya bernilai 1, jika tidak maka ditetapkan ke 0:
6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
'''

# ^ (XOR)
print(6 ^ 3) #Output: 5
''''
'Operator ^ membandingkan setiap bit dan menetapkannya ke 1 jika hanya satu yang bernilai 1, 
jika tidak (jika keduanya bernilai 1 atau keduanya bernilai 0) ditetapkan ke 0:
6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
'''

# ~ (NOT)
print(~6) #Output: -7
''''
Operator ~ membalikkan setiap bit (0 menjadi 1 dan 1 menjadi 0).'
3 terbalik menjadi -4:
 3 = 0000000000000011
-4 = 1111111111111100
Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
'''

# << (Zero fill left shift)
print(3 << 2) #Output: 12
"""
Operator << memasukkan sejumlah angka 0 yang ditentukan (dalam kasus ini 2) dari kanan dan membiarkan jumlah bit paling kiri yang sama jatuh:

Jika Anda memasukkan 00 dari kiri:
3 = 0000000000000011
menjadi
12 = 00000000000001100
Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""



# >> (Signed right shift)
print(8 >> 2) #Output: 2
"""
Operator >> memindahkan setiap bit ke kanan sejumlah yang ditentukan. Lubang kosong di sebelah kiri diisi dengan angka 0.
Jika Anda memindahkan setiap bit 2 kali ke kanan, 8 menjadi 2:
8 = 0000000000001000
menjadi
2 = 0000000000000010
Angka desimal dan nilai binernya:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
""" 

print("\n")

#Operator Prioritas
##prioritas operator menentukan urutan operasi.

#Example
print((6 + 3) - (6 + 3)) #Output: 0
#9 - 9 = 0

#perkalian dan pembagian memiliki prioritas yang lebih tinggi dari penambahan dan pengurangan.
print(100 + 5 * 3) #Output: 115
#5 * 3 = 15
#100 + 15 = 115


#jika dua operator memiliki prioritas yang sama, urutan operasi adalah dari kiri ke kanan.
print(5 + 4 - 7 + 3) #Output: 5
#5 + 4 = 9
#9 - 7 = 2
#2 + 3 = 5


