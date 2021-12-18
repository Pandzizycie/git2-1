sex = input('[k]obieta czy [m]ezczyzna ?:')
if sex == 'k':
    print('mozesz uzywac aplikacje Droga Pani')
    wiek = input("Podaj wiek: ")
    # Sprawdzamy, czy wiek jest złożony z cyfr
    if wiek.isdigit() == False:
        exit("Wiek musi być liczbą")
    wiek = int(wiek)
    if wiek >= 21 and wiek <= 65:
        print("Witamy w aplikacji i smacznej degustacji!")
    elif wiek > 65:
        print("Jesteś już za stary/a na alkohol")
    else:
        exit('jesteś za młody/a!, w USA wymagamy 21 lat')
elif sex =='m':
    print('Ta aplikacja nie jest dla facetow, sorry!')

else:
    print('Wybrano nieoslugiwana wartosci. Aplikacja jest tylko dla pelnoletnich kobiet. Sprobuj ponownie')
