def dodawanie(liczba1,liczba2):
    return liczba1+liczba2
def odejmowanie(liczba1,liczba2):
    return liczba1-liczba2
def mnozenie(liczba1,liczba2):
    return liczba1*liczba2
def dzielenie(liczba1,liczba2):
    return liczba1/liczba2
Koniec = "tak"
while Koniec.lower()=="tak":
    liczba1=float(input("Podaj 1 Liczbę: "))
    liczba2=float(input("Podaj 2 Liczbę: "))
    operacja=input("Podaj operację: [+] [-] [*] [/]: ")
    if operacja == "+":
        wynik=dodawanie(liczba1,liczba2)
        print(f"Wynik operacji to: {wynik}")
    elif operacja == "-":
        wynik=odejmowanie(liczba1,liczba2)
        print(f"Wynik operacji to: {wynik}")
    elif operacja == "*":
        wynik=mnozenie(liczba1,liczba2)
        print(f"Wynik operacji to: {wynik}")
    elif operacja == "/":
        if liczba2==0:
            print("Nie dziel przez 0!, wprowadź nowe liczby ponizej: ")
            liczba1=float(input("Podaj 1 Liczbę: "))
            liczba2=float(input("Podaj 2 Liczbę: "))
            wynik=dzielenie(liczba1,liczba2)
            print(f"Wynik operacji to: {wynik}")
        else:
            wynik=dzielenie(liczba1,liczba2)
            print(f"Wynik operacji to: {wynik}")
    else:
        print("Nieznana operacja !")
    Koniec=input("Czy chcesz powtórzyć operację dla danych liczb? Wpisz 'Tak' lub 'Nie' by zakonczyc dzialanie programu: ")
    if Koniec.lower()=="nie":
        break