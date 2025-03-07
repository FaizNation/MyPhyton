# Anda tidak dapat menyalin daftar hanya dengan mengetik list2 = list1,
# karena: list2hanya akan menjadi referensi ke list1, dan perubahan yang dibuat dalam list1akan secara otomatis juga dibuat dalam list2.

# Use the copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Use the list() method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Use the slice Operator
# You can also make a copy of a list by using the : (slice) operator.
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)