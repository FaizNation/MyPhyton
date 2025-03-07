'''
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".
'''
#You can display a string literal with the print() function:
print("Hello")
print('Hello')

print("====================================")
#You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
print("It's alright")
print('He said "Python is awesome"')
print("He said 'Python is awesome'")

print("====================================")
#Menetapkan string ke variabel dilakukan dengan nama variabel diikuti tanda sama dengan dan string:
a = "Hello"
print(a)

print("====================================")
#kita dapat menetapkan string multiline ke suatu variabel dengan menggunakan tiga tanda kutip:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

print("====================================")
#Or three single quotes:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Note: pada hasil, jeda baris disisipkan pada posisi yang sama seperti dalam kode.

print("====================================")
#Strings are arrays
#Dapatkan karakter pada posisi 1 (ingat bahwa karakter pertama memiliki posisi 0):
a = "Hello, World!"
print(a[1])

print("====================================")
#Loop through a string
#Ulangi huruf-huruf dalam kata "banana":
for x in "banana":
  print(x)

print("====================================")
#String Length
#Fungsi ini len() mengembalikan panjang string:
a = "Hello, World!"
print(len(a))

print("====================================")
#Check String
#Untuk memeriksa apakah frasa atau karakter tertentu ada dalam suatu string, kita dapat menggunakan kata kunci in.
#Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

#use it in an if statement:
#Print only if "free" is present:

if "free" in txt:
    print("Yes, 'free' is present.")

print("====================================")
#Check if NOT
#Untuk memeriksa apakah frasa atau karakter tertentu TIDAK ada dalam suatu string, kita dapat menggunakan kata kunci not in.
#Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)

#use it in an if statement:
#Print only if "expensive" is NOT present:

if "expensive" not in txt:
    print("Yes, 'expensive' is NOT present.")   

