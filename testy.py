lok = input("Podaj lokalizacje [e] (Europa) lub [us] (Stany Zjednoczone): ")
if lok == 'e':
    plec = input("Podaj plec [K] (kobieta) lub [M] (mezyczyzna): ")

    if plec == 'K':
        wiek = input("Podaj wiek: ")
        # Sprawdzamy, czy wiek jest złożony z cyfr
        if wiek.isdigit() == False:
            exit("Wiek musi być liczbą")
        wiek = int(wiek)
        if wiek >= 18 and wiek <= 65:
            print("Witamy!")
        elif wiek > 65:
            print("Jesteś już za stara na alkohol")
        else:
            exit('jesteś za młoda! W USA wymagamy 21 lat')

    elif plec == "M":
        print("Ta alikacja nie jest dla facetow, sorry")
    else:
        exit("Wybrano nieobslugiwana wartosc. Aplikacja jest tylko dla pelnoletnich kobiet. Sprobuj ponownie")

elif lok == 'us':
    plec = input("Podaj plec [K] (kobieta) lub [M] (mezyczyzna): ")

    if plec == 'K':
        wiek = input("Podaj wiek: ")
        # Sprawdzamy, czy wiek jest złożony z cyfr
        if wiek.isdigit() == False:
            exit("Wiek musi być liczbą")
        wiek = int(wiek)
        if wiek >= 21 and wiek <= 65:
            print("Witamy!")
        elif wiek > 65:
            print("Jesteś już za stara na alkohol")
        else:
            exit('jesteś za młoda! W USA wymagamy 21 lat')

    elif plec == "M":
        print("Ta alikacja nie jest dla facetow, sorry")
    else:
        exit("Wybrano nieobslugiwana wartosc. Aplikacja jest tylko dla pelnoletnich kobiet. Sprobuj ponownie")
else:
    exit("Wybrano nieobslugiwana wartosc. Aplikacja jest tylko dla mieszkancow Europy lub Stanow Zjednoczonych. Sprobuj ponownie")
