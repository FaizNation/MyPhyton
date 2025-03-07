#Variabel adalah wadah untuk menyimpan nilai data.

#example
x = 5
y = "John"
print(x) #output: 5
print(y) #output: John

#Variabel tidak perlu dideklarasikan dengan tipe data tertentu dan dapat bahkan berubah setelah mereka ditetapkan.
x = 4 # x adalah integer
x = "Sally" # x sekarang string
print(x) #output: Sally

#casting
#Jika Anda ingin menentukan tipe data variabel, Anda dapat menggunakan casting.
x = str(3) # x akan menjadi '3'
y = int(3) # y akan menjadi 3
z = float(3) # z akan menjadi 3.0 

print(x) #output: '3'
print(y) #output: 3
print(z) #output: 3.0

#Get the type
#Anda dapat mendapatkan tipe data dari variabel dengan menggunakan fungsi type().
x = 5
y = "John"
print(type(x)) #output: <class 'int'>
print(type(y)) #output: <class 'str'>   

#Single or Double Quotes?
#String dalam Python dideklarasikan dengan tanda kutip tunggal atau ganda.
x = "John"
#sama dengan
x = 'John'

#Case-Sensitive
#nama variabel (variabel) bersifat case-sensitive (besar kecil huruf berbeda).
a = 4
A = "Sally"
#A tidak sama dengan a
