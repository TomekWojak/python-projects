precision = 2
def kalkulator():
    a = float(input('Podaj pierwszą liczbę: '))
    b = float(input('Podaj drugą liczbę: '))

    print(f'Wynik działania {a} + {b}: {round(a + b, precision)}')
    print(f'Wynik działania {a} - {b}: {round(a - b, precision)}')
    print(f'Wynik działania {a} * {b}: {round(a * b, precision)}')

    if(b == 0):
        print('Nie można dzielić przez 0!')
    else:
        print(f'Wynik działania {a} / {b}: {round(a / b, precision)}')

    print(f'Wynik działania {a} do potęgi {b}: {round(a ** b, precision)}')


kalkulator()
