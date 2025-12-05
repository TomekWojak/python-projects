import math

def obliczKwadrat():
    try:
        a = float(input('Podaj liczbę: '))
        b = math.pow(a,2)
        print(f'Kwadrat liczby {a} wynosi {round(b,4)}')
    except ValueError:
        print('Podaj poprawną wartość!')


obliczKwadrat()