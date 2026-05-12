slownik={}
while True:
    try:
        dzialanie=int(input(("Wybierz działanie do wykonania [1] Dodaj hasło, [2] Wyświetl hasła, [3] Usuń hasła, [4] Wyjdź :")))
    except ValueError:
        print("Podana wartość nie jest liczbą, spróbuj ponownie.")
        continue
    if dzialanie==1:
        serwis=input("Podaj nazwe serwisu: ")
        haslo=input("Podaj haslo: ")
        slownik[serwis] = haslo
        print("Dodano ! ")
    elif dzialanie==2:
        if len(slownik)==0:
            print("Słownik jest pusty")
        else:
            for serwis, haslo in slownik.items():
                print(f"{serwis} : {haslo}")
    elif dzialanie==3:
        if len(slownik)==0:
            print("Słownik jest pusty")
        else:
            for serwis, haslo in slownik.items():
                print(f"{serwis} : {haslo}")
            DoUsuniecia=input("Wprowadz nazwe portalu: ")
            if DoUsuniecia in slownik:
                del slownik[DoUsuniecia]
                print(f"Usunięto {DoUsuniecia}!")
            else:
                print("Nie ma takiego serwisu!")
    elif dzialanie==4:
        print("Program zakonczyl dzialanie.")
        break
    else:
        print("Działanie nieznane")