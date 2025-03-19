from tabulate import tabulate #1

class Pet: #2
    def __init__(self, ras, harga, stok, jenis, diskon, habitat): #2
        self.ras = ras
        self.harga = harga
        self.stok = stok
        self.jenis = jenis
        self.diskon = diskon
        self.habitat = habitat

def display_judul():
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║                  Selamat datang di Pet Shop                      ║")
    print("║                  Temukan sahabat terbaikmuu                      ║")
    print("╚══════════════════════════════════════════════════════════════════╝")

def display_menu():
        print("\n╔══════════════════════════════════════════════════════════════════╗")
        print("║                       Daftar Menu Pet Shop                       ║")
        print("╠══════════════════════════════════════════════════════════════════╣")
        print("║ 1. ║ Tampilkan semua pet                                         ║")
        print("║ 2. ║ Cari pet berdasarkan harga                                  ║")
        print("║ 3. ║ Cari pet berdasarkan jenis                                  ║")
        print("║ 4. ║ Beli pet                                                    ║")
        print("║ 5. ║ Keluar                                                      ║")
        print("╚══════════════════════════════════════════════════════════════════╝")

def display_pets(): #3
    print("\n╔══════════════════════════════════════════════════════════════════╗")
    print("║                          Daftar Pet                              ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    headers = ["No", "Ras", "Harga", "Stok", "Diskon", "Habitat"]#4
    data = [[idx+1, pet.ras, f"Rp{pet.harga:,.2f}", pet.stok, f"{pet.diskon*100:.0f}%", pet.habitat] for idx, pet in enumerate(list_pet)]
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

def Display_cari_pet_berdasar_harga():#5
    try:#6
        harga = int(input("Masukkan harga pet yang dicari: "))#7
        found = [pet for pet in list_pet if pet.harga == harga]
        if found:#8
            for pet in found:
                print(f"{pet.ras} - Harga: Rp{pet.harga:,.2f} - Stok: {pet.stok}")
        else:#9
            print("╔══════════════════════════════════════════════════════════════════╗")
            print("║[INFO] Tidak ada pet dengan harga tersebut.                       ║")
            print("╚══════════════════════════════════════════════════════════════════╝")
    except ValueError:#9
        print("╔══════════════════════════════════════════════════════════════════╗")
        print("║[ERROR] Masukkan angka yang valid.                                ║")
        print("╚══════════════════════════════════════════════════════════════════╝")
  

def display_cari_pet_berdasar_jenis():#10
    jenis = input("Masukkan jenis pet yang dicari: ").capitalize()#11
    found = [pet for pet in list_pet if pet.jenis == jenis]#12
    if found:
        for pet in found:
            print(f"{pet.ras} - Harga: Rp{pet.harga:,.2f} - Stok: {pet.stok}")
    else:
        print("╔══════════════════════════════════════════════════════════════════╗")
        print("║[INFO] Tidak ada pet dengan jenis tersebut.                       ║")
        print("╚══════════════════════════════════════════════════════════════════╝")

def display_beli_pet():#13
    display_pets()
    try:
        ras = input("Masukkan ras pet yang ingin dibeli: ").capitalize()
        jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))
        for pet in list_pet:
            if pet.ras == ras:
                if pet.stok >= jumlah:
                    pet.stok -= jumlah
                    total_harga = jumlah * pet.harga * (1 - pet.diskon)#14
                    print("══════════════════════════════════════════════════════════════════")
                    print(f"Anda membeli {jumlah} {pet.ras} seharga Rp{total_harga:,.2f}")
                else:
                    print("╔══════════════════════════════════════════════════════════════════╗")
                    print("║[INFO] Stok tidak mencukupi.                                      ║")
                    print("╚══════════════════════════════════════════════════════════════════╝")
                return
        print("╔══════════════════════════════════════════════════════════════════╗")
        print("║[INFO] Pet tidak ditemukan.                                       ║")
        print("╚══════════════════════════════════════════════════════════════════╝")
    except ValueError:
        print("╔══════════════════════════════════════════════════════════════════╗")
        print("║[ERROR] Masukkan angka yang valid.                                ║")
        print("╚══════════════════════════════════════════════════════════════════╝")

def display_by_FadlyFais():
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║           Terima kasih telah berkunjung ke Pet Shop!             ║")
    print("║                       SEMANGAT PUASANYA!!!                       ║")
    print("║                                                                  ║")
    print("║               By Fadly Fais Fajarruddin_24111814015              ║")
    print("╚══════════════════════════════════════════════════════════════════╝")

list_pet = [ #15
    Pet("Persia", 1500000, 10, "Kucing", 0.1, "Darat"),
    Pet("Anggora", 1400000, 8, "Kucing", 0.08, "Darat"),
    Pet("Golden", 3000000, 5, "Anjing", 0.1, "Darat"),
    Pet("Koi", 500000, 20, "Ikan", 0.1, "Air"),
    Pet("Kakaktua", 2500000, 8, "Burung", 0.1, "Udara"),
]

if __name__ == "__main__":#16
    display_judul()
    while True: #17
        display_menu()
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            display_pets()
        elif pilihan == "2":
            Display_cari_pet_berdasar_harga()
        elif pilihan == "3":
            display_cari_pet_berdasar_jenis()
        elif pilihan == "4":
            display_beli_pet()
        elif pilihan == "5":
            display_by_FadlyFais()
            break
        else:
            print("╔══════════════════════════════════════════════════════════════════╗")
            print("║[INFO] Pilihan tidak valid.                                       ║")
            print("╚══════════════════════════════════════════════════════════════════╝")
            

'''
Ppenjelasan kode berdasarkan nomor yang saya berikan:  

1 from tabulate import tabulate
   - Mengimpor tabulate, yang digunakan untuk menampilkan data dalam format tabel yang lebih rapi.

2 class Pet dan __init__
   - Kelas Pet digunakan untuk merepresentasikan setiap hewan peliharaan di toko.
   - Konstruktor __init__ menginisialisasi atribut untuk setiap pet:
     - ras      : Jenis ras pet.
     - harga    : Harga pet dalam mata uang.
     - stok     : Jumlah stok yang tersedia.
     - jenis    : Jenis pet (misalnya Kucing, Anjing, Burung, dll.).
     - diskon   : Persentase diskon untuk pet.
     - habitat  : Tempat hidup pet (darat, air, udara).

3 function display_pets()
   - Menampilkan daftar pet dalam bentuk tabel menggunakan tabulate.
   - Menampilkan kolom Nomor, Ras, Harga, Stok, Diskon, Habitat.
   - Data ditampilkan dalam format "fancy_grid" agar lebih rapi.

4 headers dan data
   - Membuat daftar header yang akan digunakan dalam tabel (`No`, `Ras`, `Harga`, `Stok`, `Diskon`, `Habitat`).

5 function Display_cari_pet_berdasar_harga()
   - Untuk pengguna mencari pet berdasarkan harga tertentu.
   - Jika harga yang dimasukkan ada dalam daftar, maka informasi pet akan ditampilkan.
   - Jika tidak ditemukan, akan muncul pesan informasi.

6 try
   - Blok try-except digunakan untuk menangani kemungkinan kesalahan input.
   - Jika pengguna memasukkan input yang bukan angka, maka akan ditangani di bagian `except`.

7 harga = int(input("Masukkan harga pet yang dicari: "))
   - Menerima input dari pengguna untuk mencari pet berdasarkan harga.
   - int(input(...)) memastikan bahwa input yang dimasukkan adalah angka.

8 if found
   - Memeriksa apakah ada pet yang cocok dengan harga yang dimasukkan oleh pengguna.
   - Jika ditemukan, maka pet tersebut akan ditampilkan.

9 else: & `except ValueError
   - else Jika tidak ada pet yang cocok dengan harga yang dicari, maka akan ditampilkan pesan bahwa pet tidak ditemukan.
   - except ValueError Jika pengguna memasukkan input yang bukan angka, akan muncul pesan kesalahan.

10 function search_pet_by_type()
   - untuk pengguna mencari pet berdasarkan jenis (misalnya Kucing, Anjing, Burung, dll.).
   - Jika ditemukan, daftar pet akan ditampilkan, jika tidak maka akan muncul pesan bahwa pet tidak ditemukan.

11 jenis = input("Masukkan jenis pet yang dicari: ").capitalize()
   - Mengambil input dari pengguna dan mengubah huruf pertama menjadi huruf besar agar formatnya konsisten dengan daftar pet.

12 found = [pet for pet in list_pet if pet.jenis == jenis]
   - Menggunakan list comprehension untuk mencari pet berdasarkan jenis yang dimasukkan pengguna.

13 display_buy_pet()
   - Memungkinkan pengguna membeli pet berdasarkan ras dan jumlah yang diinginkan.
   - Mengecek apakah stok mencukupi sebelum melakukan pembelian.

14 total_harga = jumlah * pet.harga * (1 - pet.diskon)
   - Menghitung harga total setelah diskon:
     - jumlah * pet.harga: Menghitung harga sebelum diskon.
     - (1 - pet.diskon): Mengurangi harga berdasarkan persentase diskon.

15 list_pet
   - Berisi daftar objek `Pet` yang tersedia di toko.
   - Setiap pet memiliki harga, stok, jenis, diskon, dan habitatnya masing-masing.

16 if __name__ == "__main__":
   - Memastikan bahwa kode di bawah hanya akan dijalankan jika script dieksekusi langsung.
   - Jika script diimpor sebagai modul, kode ini tidak akan dieksekusi.

17 while True
   - Membuat loop tak terbatas untuk menampilkan menu kepada pengguna.
   - Pengguna dapat terus memilih menu sampai memilih opsi "Keluar" (5).
'''