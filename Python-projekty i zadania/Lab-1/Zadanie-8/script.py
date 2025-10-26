import math

def oblicz_rownanie_kwadratowe():
    a = float(input('Podaj a: '))
    b = float(input('Podaj b: '))
    c = float(input('Podaj c: '))

    if a == 0:
        if b == 0 and c == 0:
            print('Równianie tożsamościowe')
            return
        elif b == 0:
            print('Równanie jest sprzeczne')
            return
        else:
            wynik = -c / b
            print(f'Wynik funkcji liniowej: {round(wynik, 2)}')
            return wynik


    delta = b**2 - 4 * a * c

    if delta < 0:
        print('Równanie nie ma rozwiązań w zbiorze liczb rzeczywistych')
        return

    if delta == 0:
        x1 = -b / (2 * a)
        x2 = x1
    elif delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)

    print(f'Rozwiązania równania kwadratowego dla wartości a: {a}, b: {b} i c: {c} są następujące: X1: {round(x1, 2)}, X2: {round(x2, 2)}')

oblicz_rownanie_kwadratowe()
