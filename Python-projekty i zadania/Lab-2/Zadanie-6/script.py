def sprawdzWielkoscLitery():
    while True:
        litera = input('Podaj literę lub wyraz: ').strip()

        if not litera:
            print('Wartość nie może być pusta!')
            continue
        break

    if len(litera) == 1:
        if litera == litera.upper():
            print(f'Litera {litera} jest duża')
        else:
            print(f'Litera {litera} jest mała')
    else:
        if litera[-1] == litera[-1].upper():
            print(f'Ostatnia litera podanego wyrazu - {litera}, czyli {litera[-1]} jest duża')
        else:
            print(f'Ostatnia litera podanego wyrazu - {litera}, czyli {litera[-1]} jest mała')

sprawdzWielkoscLitery()

# Program sprawdza wielkość litery podanej przez użytkownika, a w przypadku wpisania wyrazu - poda wielkość ostaniej litery