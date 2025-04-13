import socket

def get_local_ip():
    return socket.gethostbyname(socket.gethostname())  # (1)

print("Selamat datang di aplikasi chatting \nPilih posisi: \n1. Server \n2. Client")

def switch_case(case):
    match case:
        case 1:
            serverIP = get_local_ip()  # (2)
            serverPort = 2025
            serverAddr = ("0.0.0.0", serverPort)  # (3)

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(serverAddr)  # (4)
            sock.listen(1)  # (5)
            print(f"Server berjalan di {serverIP}:{serverPort}, menunggu koneksi...")

            conn, addr = sock.accept()  # (6)
            print(f"Client {addr} terhubung!")

            while True:
                try:
                    data = conn.recv(1024).decode()  # (7)
                    if not data:
                        break
                    print("Pesan dari client:", data)
                    
                    data = input("Masukkan pesan: ")  # (8)
                    conn.send(data.encode())  
                except:
                    print("Client terputus.")
                    break

            conn.close()  # (9)
                
        case 2:
            serverIP = input("Masukkan IP Server: ")  # (10)
            serverPort = 2025
            serverAddr = (serverIP, serverPort)

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            try:
                print(f"Mencoba terhubung ke server {serverIP}:{serverPort}...")
                sock.connect(serverAddr)  # (11)
                print("Terhubung ke server!")

                while True:
                    data = input("Masukkan pesan: ")  # (12)
                    sock.send(data.encode())  

                    data = sock.recv(1024).decode()  # (13)
                    if not data:
                        break
                    print("Pesan dari server:", data)
            
            except ConnectionRefusedError:
                print("Gagal terhubung ke server! Pastikan server berjalan.")  # (14)
            except:
                print("Terjadi kesalahan, koneksi terputus.")  # (15)
            finally:
                sock.close()  # (16)

        case _:
            print("Pilihan tidak tersedia")  # (17)

# (18)
try:
    pilihan = int(input("Masukkan pilihan: "))
    switch_case(pilihan)  
except ValueError:
    print("Masukkan angka yang valid!")