import socket
host=input("Podaj adres do zeskanowania: ")
for port in range(1,100):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.settimeout(1)
    result=server.connect_ex((host, port))
    if result==0:
        print(f"Port numer: {port} jest Otwarty")
    server.close()
