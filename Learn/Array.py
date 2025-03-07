## List nama mobil ##
car1 = "Ford"
car2 = "Volvo"
car3 = "Bmw"

print ("=======================================")

## List nama mobil menggunakan Array ##
cars = ["Ford", "Volvo", "BMW"]

x = cars[0] # print element pertama

print(x)

print ("=======================================")

## Mengganti element dalam Array ##
cars = ["Ford", "Volvo", "BMW"]

cars[0] = "Toyota" # mengganti element pertama

print(cars)

print ("=======================================")

# Menghitung jumlah element dalam Array #
cars = ["Ford", "Volvo", "BMW"]

x = len(cars) # len untuk menghitung jumlah element dalam Array

print(x)

print ("=======================================")

# looping dalam Array #
cars = ["Ford", "Volvo", "BMW"]

for x in cars: # looping elemen dalam Array
  print(x)

print ("=======================================")

# Menambahkan element dalam Array #
cars = ["Ford", "Volvo", "BMW"]

cars.append("Honda") # menambahkan 1 element baru dalam Array
print(cars)

print ("=======================================")

# Menghapus element dalam Array #
cars = ["Ford", "Volvo", "BMW"]

cars.pop(1) # menghapus element ke 2 dalam Array
print(cars)
