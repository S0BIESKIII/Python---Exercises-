import random 
secret_number = random.randint(1,100)
licznik=0
while True:
    try:
        liczba_uzytkownika=int(input("Podaj Swoją liczbę: "))
    except ValueError:
            print("To nie jest liczba! Wpisz cyfrę.")
            continue
    licznik=licznik+1
    if liczba_uzytkownika==secret_number:
        print(f"Udało Ci się zgadnąć za {licznik} razem!")
        break
    elif liczba_uzytkownika>secret_number:
        print("Nie udało Ci się, liczba jest za duza! Spróbuj ponownie.")    
    else:
        print("Nie udało Ci się, liczba jest za mała! Spróbuj ponownie.")