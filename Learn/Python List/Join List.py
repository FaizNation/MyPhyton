# Join Two Lists
# Salah satu cara termudah adalah dengan menggunakan + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Cara lain untuk menggabungkan dua daftar adalah dengan menambahkan semua item dari list2 ke list1, satu per satu:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# Gunakan extend()metode untuk menambahkan list2 di akhir list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
