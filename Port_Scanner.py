import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.settimeout(1)
result=server.connect_ex(('google.com', 22))
if result==0:
    print("Otwarty")
else:
    print("Zamknięty")
server.close()
