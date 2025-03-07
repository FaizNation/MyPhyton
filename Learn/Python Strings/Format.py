#F-String
#Create an f-string:
age = 36
txt = f"My name is John, I am {age}"
print(txt) #output: My name is John, I am 36    

print("====================================")
#placeholder
#Add a placeholder for the price variable:
price = 59
txt = f"The price is {price} dollars"
print(txt) #output: The price is 59 dollars

#disertakan dengan menambahkan titik dua :diikuti oleh jenis format legal, 
# seperti .2fyang berarti angka titik tetap dengan 2 desimal:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt) #output: The price is 59.00 dollars

#operasi matematika di placeholder, dan kembalikan hasilnya:
txt = f"The price is {20 * 59} dollars"
print(txt) #output: The price is 1180 dollars

