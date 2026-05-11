waga=float(input("Podaj wagę w kg: "))
wzrost=float(input("Podaj wzrost w [Metrach]: "))
if wzrost>=2.5:
    wzrost=wzrost/100
bmi=waga/(wzrost**2)
if bmi<18.5:
    print(f"BMI wynosi: {bmi:.2f} STATUS: Niedowaga")
elif bmi>=18.5 and bmi<=24.9:
    print(f"BMI wynosi: {bmi:.2f} STATUS: norma")
elif bmi>=25 and bmi<=29.9:
    print(F"BMI wynosi: {bmi:.2f} STATUS: nadwaga")
else:
    print(f"BMI wynosi: {bmi:.2f} STATUS: Otyłość")
