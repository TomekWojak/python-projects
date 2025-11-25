while True:
    try:
        a = int(input('Podaj liczbę całkowitą: '))

    except ValueError:
        print("To nie jest liczba!")
