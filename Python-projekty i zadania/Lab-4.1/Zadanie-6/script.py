import math

def obliczPole():
    try:
        a = float(input('Podaj długość boku a: '))
        b = float(input('Podaj długość boku b: '))
        c = float(input('Podaj długość boku c: '))

        if a + b <= c or a + c <= b or b + c <= a:
            print("Z podanych boków nie da się zbudować trójkąta!")
            return

        s = (a + b + c) / 2
        pole = math.sqrt(s * (s-a) * (s-b) * (s-c))
        print(f'Pole trójkąta o bokach {a}, {b} i {c} wynosi: {round(pole,2)}')

    except ValueError:
        print('Podano niepoprawną wartość!')

obliczPole()