ceny_potraw = []
def podziel_rachunek():
    while True:
        try:
            x = int(input('Podaj liczbę gości: '))
            n = int(input('Podaj liczbę potraw: '))
            break
        except ValueError:
            print("Podano nieprawidłową wartość")

    while len(ceny_potraw) < n:
        try:
            cena = float(input(f'Podaj cenę potrawy nr {len(ceny_potraw) + 1} (waluta: zł): '))
            ceny_potraw.append(cena)
        except ValueError:
            print('Podano nieprawidłową wartość!')


    suma = sum(ceny_potraw)
    srednia_cena = suma / n
    rachunek = suma / x

    print(f'Łącznie zamówiono {n} potraw. Średnia cena zamówionej potrawy wynosi {srednia_cena}zł. \nSprawiedliwie będzie jeśli podzielimy rachunek, który wynosi {suma}zł na ilość gości: {x}. Każdy z gości musi złożyć się po {rachunek}zł')


podziel_rachunek()
