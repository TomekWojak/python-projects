def oblicz_rownanie_liniowe():
    a = float(input('Podaj a: '))
    b = float(input('Podaj b: '))

    if(a == 0 and b == 0):
        print('Równianie tożsamościowe')
        return
    elif(a == 0):
        print('Równanie jest sprzeczne')
        return
    else:
        wynik = -b / a
        print(f'Wynik funkcji liniowej: {round(wynik, 2)}')


oblicz_rownanie_liniowe()