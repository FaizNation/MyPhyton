#Dapatkan karakter dari posisi 2 ke posisi 5 (tidak termasuk):
a = "Hello, World!"
print(a[2:5]) #output: llo

#Note: Karakter pertama memiliki indeks 0.

print("====================================")
#Slice From the Start
#Dapatkan karakter dari posisi 2, dan seterusnya:
b = "Hello, World!"
print(b[:5]) #output: Hello

print("====================================")
#Slice To the End
#Dapatkan karakter dari posisi 2, sampai akhir:
b = "Hello, World!"
print(b[2:]) #output: llo, World!

print("====================================")
#Negative Indexing
'''
Dapatkan karakternya:
Dari: "o" di "Dunia!" (posisi -5)
Kepada, tetapi tidak termasuk: "d" di "Dunia!" (posisi -2):
'''
b = "Hello, World!"
print(b[-5:-2]) #output: orl