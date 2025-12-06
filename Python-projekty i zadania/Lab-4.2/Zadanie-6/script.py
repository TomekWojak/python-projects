import time


def sekundnik():
    try:
        czas = int(input('Podaj czas (w sekundach): '))

        while czas >= 0:
            print(f'Liczba sekund pozostała do końca: {czas}s')
            if czas == 0: print('Koniec czasu!')
            time.sleep(1)
            czas -= 1


    except ValueError:
        print('Podaj poprawny czas!')

sekundnik()