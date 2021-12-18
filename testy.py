wiek = input("Podaj wiek: ")
# Sprawdzamy, czy wiek jest złożony z cyfr
if wiek.isdigit() == False:
    exit("Wiek musi być liczbą")
wiek = int(wiek)
if wiek >= 21 and wiek <= 65:
    print("Witamy!")
elif wiek > 65:
    print("Jesteś już za stary na alkohol")
else:
    exit('jesteś za młody!, w USA wymagamy 21 lat')
