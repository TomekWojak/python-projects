def oblicz_rownanie_liniowe():
    a = float(input('Podaj a: '))

    while(a == 0):
        print('a nie może być równe 0!')
        a = float(input('Podaj a: '))


    b = float(input('Podaj b: '))

    wynik = -b / a
    print(f'Wynik funkcji liniowej: {round(wynik, 2)}')

oblicz_rownanie_liniowe()