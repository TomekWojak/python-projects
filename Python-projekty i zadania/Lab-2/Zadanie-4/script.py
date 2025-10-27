PUNKTY_ZA_BRAMKE = 10
BONUS_ZA_5_BRAMEK = 5
BONUS_ZA_10_BRAMEK = 10

def obsluzFunkcjeMenedzeraFootbolu():
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


def obliczWynikDruzyny(gol):
    liczbaBramek = int(gol)
    wynikZaBramki = liczbaBramek * PUNKTY_ZA_BRAMKE
    bonus = 0

    if liczbaBramek > 10:
        bonus = BONUS_ZA_5_BRAMEK + BONUS_ZA_10_BRAMEK
    elif liczbaBramek > 5:
        bonus = BONUS_ZA_5_BRAMEK

    calkowityWynik = wynikZaBramki + bonus

    print(f'Drużyna uzyskała {wynikZaBramki} punktów za strzelone gole \nCałkowity wynik drużyny wynosi {calkowityWynik} punktów')

obsluzFunkcjeMenedzeraFootbolu()