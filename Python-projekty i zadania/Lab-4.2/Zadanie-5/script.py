import random

ZAKRES_NUMEROW = 50
ILOSC_KUL = 6
listaNumerow = list(range(1,ZAKRES_NUMEROW))


def wylosujKule():
    wylosowaneKule = random.sample(listaNumerow, ILOSC_KUL)
    return wylosowaneKule

print(f'Wylosowane kule: {wylosujKule()}')
