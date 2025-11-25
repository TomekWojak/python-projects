while True:
    try:
        a = int(input('Podaj liczbę całkowitą: '))
    except ValueError:
        print("To nie jest liczba!")

    if(a < 0):
        print(f'{a} jest mniejsze od 0')
        break