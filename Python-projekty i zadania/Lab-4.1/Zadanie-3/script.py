import json
with open("translations.json", "r", encoding="utf-8") as file:
    tlumaczenia = json.load(file)


def powitanie(imie="Użytkowniku",jezyk="Polski"):
    try:
        jezykPowitania = tlumaczenia[jezyk.lower()]
        print(f'{jezykPowitania}, {imie}')
    except KeyError:
        print(f'Witaj, {imie}')



powitanie('Bartek', 'polski')
powitanie('Maciej', 'angielski')
powitanie('Jan', 'niemiecki')
powitanie('Zosia', 'ANGIELSKI')
powitanie('Kasia', 'pl')

