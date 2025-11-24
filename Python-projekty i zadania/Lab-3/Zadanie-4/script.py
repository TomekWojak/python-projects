ceny_potraw = []
def podziel_rachunek():
    x = int(input('Podaj liczbę gości: ') or 0)
    n = int(input('Podaj liczbę potraw: ') or 0)

    while len(ceny_potraw) < n:
        cena = float(input('Podaj cenę pierwszej potrawy (waluta: zł): ') or 0)
        ceny_potraw.append(cena)

    suma = sum(ceny_potraw)
    srednia_cena = suma / n
    rachunek = suma / x

    print(f'Łącznie zamówiono {n} potraw. Średnia cena zamówionej potrawy wynosi {srednia_cena}zł. \nSprawiedliwie będzie jeśli podzielimy rachunek, który wynosi {suma}zł na ilość gości: {x}. Każdy z gości musi złożyć się po {rachunek}zł')


podziel_rachunek()
