'''
Variabel yang dibuat di luar suatu fungsi dikenal sebagai variabel global
Variabel global dapat digunakan oleh siapa saja, baik di dalam fungsi maupun di luar.
'''
#example
#buat variabel di luar fungsi, dan gunakan di dalam fungsi
x = "awesome"

def myfunc():
    print("Python is " + x)


myfunc()

print("====================================")
'''
Jika Anda membuat variabel dengan nama yang sama di dalam suatu fungsi, 
variabel ini akan bersifat lokal, dan hanya dapat digunakan di dalam fungsi tersebut. 
Variabel global dengan nama yang sama akan tetap seperti sebelumnya, global dan dengan nilai aslinya.
'''
#example
#membuat variabel di dalam fungsi, dengan nama yang sama dengan variabel global
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

print("====================================")
#The global Keyword
'''
Biasanya, ketika Anda membuat suatu variabel di dalam suatu fungsi,
variabel tersebut bersifat lokal, dan hanya dapat digunakan di dalam fungsi tersebut.
Untuk membuat variabel global di dalam suatu fungsi, Anda dapat menggunakan global keyword.
'''
#example
#Jika Anda menggunakan globalkata kunci, variabel tersebut termasuk dalam cakupan global:
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

print("====================================")
#Also, use the global keyword if you want to change a global variable inside a function.
#example
#Untuk mengubah nilai variabel global di dalam suatu fungsi, rujuk variabel tersebut dengan menggunakan global keyword:
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

