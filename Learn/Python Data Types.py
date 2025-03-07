'''
Python memiliki tipe data bawaan berikut, dalam kategori berikut:
Text Type:	    str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	    set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	    NoneType
'''
#Anda bisa mendapatkan tipe data objek apa pun dengan menggunakan type()fungsi:
x = 5
print(type(x)) #output: <class 'int'>

#Dalam Python, tipe data ditetapkan saat Anda menetapkan nilai ke variabel:

print("====================================")
#example data str
x = "Hello World"
print(x) #output: Hello World
print(type(x)) #output: <class 'str'>

print("====================================")
#example data int
x = 20
print(x) #output: 20
print(type(x)) #output: <class 'int'>

print("====================================")
#example data float
x = 20.5
print(x) #output: 20.5
print(type(x)) #output: <class 'float'>

print("====================================")
#example data complex
x = 1j
print(x) #output: 1j
print(type(x)) #output: <class 'complex'>

print("====================================")
#example data list
x = ["apple", "banana", "cherry"]
print(x) #output: ['apple', 'banana', 'cherry']
print(type(x)) #output: <class 'list'>

print("====================================")
#example data tuple
x = ("apple", "banana", "cherry")
print(x) #output: ('apple', 'banana', 'cherry')
print(type(x)) #output: <class 'tuple'>

print("====================================")
#example data range
x = range(6)
print(x) #output: range(0, 6)
print(type(x)) #output: <class 'range'>

print("====================================")
#example data dict
x = {"name" : "John", "age" : 36}
print(x) #output: {'name': 'John', 'age': 36}
print(type(x)) #output: <class 'dict'>

print("====================================")
#example data set
x = {"apple", "banana", "cherry"}
print(x) #output: {'banana', 'apple', 'cherry'}
print(type(x)) #output: <class 'set'>

print("====================================")
#example data frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x) #output: frozenset({'banana', 'apple', 'cherry'})
print(type(x)) #output: <class 'frozenset'>

print("====================================")
#example data bool
x = True
print(x) #output: True
print(type(x)) #output: <class 'bool'>

print("====================================")
#example data bytes
x = b"Hello"
print(x) #output: b'Hello'
print(type(x)) #output: <class 'bytes'>

print("====================================")
#example data bytearray
x = bytearray(5)
print(x) #output: bytearray(b'\x00\x00\x00\x00\x00')
print(type(x)) #output: <class 'bytearray'>

print("====================================")
#example data memoryview
x = memoryview(bytes(5))
print(x) #output: <memory at 0x7f8f7c6f1d00>
print(type(x)) #output: <class 'memoryview'>

print("====================================")   
#example data None
x = None
print(x) #output: None
print(type(x)) #output: <class 'NoneType'>