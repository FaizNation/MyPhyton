#Untuk menyisipkan karakter yang ilegal dalam suatu string, gunakan karakter escape.
#Karakter escape adalah garis miring terbalik \diikuti oleh karakter yang ingin Anda masukkan

txt = "We are the so-called \"Vikings\" from the north."
print(txt)
#output: We are the so-called "Vikings" from the north.

print("====================================")
'''
Escape Characters
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value'
'''
#single quote
txt = 'It\'s alright.'
print(txt) #output: It's alright.

print("====================================")
#backslash
txt = "This will insert one \\ (backslash)."
print(txt) #output: This will insert one \ (backslash).

print("====================================")
#new line
txt = "Hello\nWorld!"
print(txt) #output: Hello
           #        World!

print("====================================")
#Carriage Return
txt = "Hello\rWorld!"
print(txt) #output: World!

print("====================================")
#Tab
txt = "Hello\tWorld!"
print(txt) #output: Hello    World!

print("====================================")
#Backspace
txt = "Hello \bWorld!"
print(txt) #output: HelloWorld!

print("====================================")

#Form Feed
txt = "Hello\fWorld!"
print(txt) #output: Hello
           #        World!  

print("====================================")
#Octal value
txt = "\110\145\154\154\157"
print(txt) #output: Hello

print("====================================")
#Hex value
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) #output: Hello