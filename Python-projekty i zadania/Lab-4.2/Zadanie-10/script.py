import random
import math

def nazwaFunkcji():
    try:
        print('Podaj przedział, z którego program ma losować liczby')
        a = int(input('Podaj początek przedziału: '))
        b = int(input('Podaj koniec przedziału (włącznie): '))
        if(a > b):
            print('Początek przedziału musi mieć mniejszą wartość niż jego koniec!')
            return

        krotka = tuple(wylosujLiczbe(a,b) for _ in range(10))
        print(f'Wylosowane liczby z przedziału {a}-{b}: {krotka}')
        print(f'Średnia geometryczna wylosowanych liczb wynosi: {round(obliczSrednia(krotka),2)}')


    except ValueError:
        print('Podaj poprawny zakres!')

def obliczSrednia(krotka):
    return math.prod(krotka) ** (1 / len(krotka))
def wylosujLiczbe(a,b):
    liczba = random.randint(a,b)
    return liczba

nazwaFunkcji()