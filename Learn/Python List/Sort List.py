# Sort List Alphanumerically
# Objek daftar memiliki sort()metode yang akan mengurutkan daftar secara alfanumerik, menaik, secara default:
#example berdasar abjad
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# examle berdasar numerik
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort Descending
# Untuk mengurutkan secara menurun, gunakan argumen kata kunci reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

print("\n")

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# Customize Sort Function
# Anda juga dapat menyesuaikan fungsi Anda sendiri dengan menggunakan argumen kata kunci .key = function
# Fungsi ini akan mengembalikan angka yang akan digunakan untuk mengurutkan daftar (angka terendah terlebih dahulu)
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# Case Insensitive Sort
# Secara default, sort()metode ini peka huruf besar/kecil, sehingga semua huruf kapital akan diurutkan terlebih dahulu sebelum huruf kecil:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# pengurutan daftar tanpa memperhatikan huruf besar/kecil:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Reverse Order
# Metode ini reverse()membalik susunan penyortiran elemen saat ini.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


