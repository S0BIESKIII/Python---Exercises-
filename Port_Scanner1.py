import socket
ports={21:"FTP",22:"SSH",23:"Telnet",25:"SMTP",53:"DNS",80:"HTTP",443:"HTTPS"}
host=input("Podaj adres do zeskanowania: ")
start=int(input("Start: "))
koniec=int(input("Koniec: "))
for port in range(start,koniec):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.settimeout(1)
    result=server.connect_ex((host, port))
    if result==0:
        nazwa = ports.get(port, "Nieznana")
        print(f"Port {port} ({nazwa}) jest Otwarty")
    server.close()
