lista_zakupow = {
    "chleb": 4.50,
    "masło": 8.20,
    "mleko": 3.80,
    "10 jajek": 9.50,
    "ser żółty": 22.90,
    "szynka": 28.40,
    "Kilo jabłek": 4.20,
    "Kilo bananów": 5.10,
    "makaron": 3.60,
    "ryż": 4.30,
    "cukier": 3.40,
    "mąka": 2.80,
    "jogurt naturalny": 2.10,
    "kurczak": 14.90,
    "woda mineralna": 1.80
}
print(lista_zakupow)
suma_wydatkow = sum(lista_zakupow.values())
print(f'Suma wydatków wynosi: {suma_wydatkow} zł')