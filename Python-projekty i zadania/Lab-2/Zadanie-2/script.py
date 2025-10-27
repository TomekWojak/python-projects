mapaWartosci = {
    "mal": "malejąco",
    "ros": "rosnąco"
}
def obsluzWalidacjeDanych():
    while True:
        x = input('Podaj x: ')
        y = input('Podaj y: ')
        z = input('Podaj z: ')
        warunek = input('Liczby mają być uporządkowane rosnąco czy malejąco? [mal / ros]: ')

        if(not x or not y or not z or not warunek):
            print('Podano nieprawidłowe wartości!')
            continue
        else:
            try:
                if warunek != 'mal' and warunek != 'ros':
                    print(f'{warunek} jest nieprawidłowym warunkiem!')
                    continue

                uporzadkowaneLiczby = uporzadkujLiczby(warunek, x, y, z)
                print(f'Liczby uporządkowane {mapaWartosci[warunek]} prezentują się w następujący sposób: {uporzadkowaneLiczby}')
                break
            except ValueError:
                print('Podano nieprawidłowe wartości!')

def uporzadkujLiczby(warunek, val1, val2, val3):
    x = float(val1)
    y = float(val2)
    z = float(val3)

    if warunek == 'ros':
        if (x > y): x, y = y, x
        if (y > z): y, z = z, y
        if (x > y): x, y = y, x
    elif warunek == 'mal':
        if (x < y): x, y = y, x
        if (x < z): x, z = z, x
        if (y < z): y, z = z, y

    return [x, y, z]

obsluzWalidacjeDanych()

# Dodałem możliwość wybrania przez użytkownika, w jaki sposób sortować liczby. Zastosowałem również obiekt mapujący, aby potwierdzić wybór użytkownika
# Dla lepszego UX, zastosowałem dodatkowy warunek sprawdzający wartość zmiennej "warunek", po to aby użytkownik wiedział dokładniej gdzie jest bład.
