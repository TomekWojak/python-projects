def oblicz_rownanie_kwadratowe():
    a = float(input('Podaj a: '))
    b = float(input('Podaj b: '))
    c = float(input('Podaj c: '))

    x1 = None
    x2 = None

    delta = b * b - 4 * a * c

    if delta < 0:
        print('Równanie nie ma rozwiązań w zbiorze liczb rzeczywistych')
        return

    if delta == 0:
        x1 = -b / (2 * a)
        x2 = x1
    elif delta > 0:
        x1 = (-b - (delta** 0.5)) / (2 * a)
        x2 = (-b + (delta** 0.5)) / (2 * a)

    print(f'Rozwiązania równania kwadratowego dla wartości a: {a}, b: {b} i c: {c} są następujące: X1: {round(x1, 2)}, X2: {round(x2, 2)}')

oblicz_rownanie_kwadratowe()


