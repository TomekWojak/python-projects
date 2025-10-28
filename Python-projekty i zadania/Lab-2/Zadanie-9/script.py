def zamienWielkosciLiter():
    while True:
        text = input('Podaj literę lub wyraz: ')

        if not text:
            print('Wartość nie może być pusta!')
            continue
        break

    zamienioneWielkosci = text.swapcase()
    print(zamienioneWielkosci)

zamienWielkosciLiter()