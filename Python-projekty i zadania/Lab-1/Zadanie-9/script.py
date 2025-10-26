precyzja = 2
maksymalnaPotęga = 20

def miniKalkulator():
    a = float(input('Podaj pierwszą liczbę: '))
    b = float(input('Podaj drugą liczbę: '))

    print(f'Wynik działania {a} + {b}: {round(a + b, precyzja)}')
    print(f'Wynik działania {a} - {b}: {round(a - b, precyzja)}')
    print(f'Wynik działania {a} * {b}: {round(a * b, precyzja)}')

    if b == 0:
        print('Nie można dzielić przez 0!')
    else:
        print(f'Wynik działania {a} / {b}: {round(a / b, precyzja)}')

    if abs(b) > maksymalnaPotęga:
        print(f'Wynik działania {a} do potęgi {b}: Za duża potęga!')
    else:
        print(f'Wynik działania {a} do potęgi {b}: {round(a ** b, precyzja)}')


miniKalkulator()