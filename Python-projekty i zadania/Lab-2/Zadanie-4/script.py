def obsluzWalidacje():
    while True:
        gol = input('Podaj liczbę strzelonych bramek: ')

        if not gol:
            print('Liczba strzelonych bramek nie może być pusta!')
            continue
        else:
            try:
                obliczWynikDruzyny(gol)
                break
            except ValueError:
                print('Podano niepoprawne dane!')




