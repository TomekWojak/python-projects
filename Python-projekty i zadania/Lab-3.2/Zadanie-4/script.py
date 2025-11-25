alfabet = set("aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż")
litery = set()

def tester_zdan():
    zdanie = input('Podaj zdanie: ').lower()

    for znak in zdanie:
        if znak in alfabet:
            litery.add(znak)

    posortowane = sorted(litery)
    przefiltrowane = alfabet - litery
    print(" ".join(posortowane))

    print(f'Zdanie: "{zdanie}" nie zawiera liter alfabetu: {",".join(przefiltrowane)}')

tester_zdan()