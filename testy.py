wiek = input("Podaj wiek: ")
# Sprawdzamy, czy wiek jest złożony z cyfr
if wiek.isdigit() == False:
    exit("Wiek musi być liczbą")
wiek = int(wiek)
if wiek >= 18 and wiek <= 40:
    print("Witamy!")
elif wiek > 40:
    print("Jesteś już za stary na alkohol")
else:
    exit('jesteś za młody!')
    
