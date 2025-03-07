#Upper case
#Metode ini upper()mengembalikan string dalam huruf besar:
a = "Hello, World!"
print(a.upper()) #output: HELLO, WORLD!

print("====================================")
#Lower case
#Metode ini lower()mengembalikan string dalam huruf kecil:
a = "Hello, World!"
print(a.lower()) #output: hello, world!

print("====================================")
#Remove Whitespace
#Metode ini strip()menghapus spasi dari awal atau akhir:
a = " Hello, World! "
print(a.strip()) #output: Hello, World!

print("====================================")
#Replace String
#Metode ini replace()menggantikan string dengan string lain:
a = "Hello, World!"
print(a.replace("H", "J")) #output: Jello, World!

print("====================================")
#Split String
#Metode ini split()membagi string menjadi beberapa substring jika menemukan contoh pemisah:
a = "Hello, World!"
print(a.split(",")) #output: ['Hello', ' World!']
