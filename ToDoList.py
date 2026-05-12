zadania = []
while True:
    try:
        print("wyświetl menu [1] Dodaj [2] Wyświetl [3] Usuń [3] [4] Wyjdź")
        operacja=int(input("Podaj numer operacji który chcesz wykonać: "))
    except ValueError:
         print("Prawdopodobnie podałeś inną wartość niz liczbowa, podaj ponownie operacje ktora chcesz wykonac: ")
         continue
    if operacja==1:
        nazwa=input("Nazwa zadania: ")
        zadania.append(nazwa)
    elif operacja==2:
        if len(zadania) == 0:
            print("Brak zadań")
        else:
            for numer, zadanie in enumerate(zadania, 1):
                print(f"{numer}. {zadanie}")
    elif operacja==3:
        if len(zadania) == 0:
            print("Brak zadań do usunięcia.")
        else:                          
            for numer, zadanie in enumerate(zadania, 1):
                print(f"{numer}. {zadanie}")
            numer=int(input("Podaj numer z listy do usunięcia: "))
            if numer < 1 or numer > len(zadania):   
                print("Nie ma zadania o tym numerze!")
            else:
                del zadania[numer - 1]
    elif operacja==4:
        print("Program zakończył działanie: ")
        break
    else:
         print("Nieznane działanie!")